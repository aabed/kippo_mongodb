from kippo.core import dblog
from twisted.python import log
from pymongo import *
import gridfs
import os
import struct
import hashlib
import json
import socket
import uuid


class DBLogger(dblog.DBLogger):
	def start(self, cfg):
		print 'mongodb DBLogger start'

		server	= cfg.get('database_mongodb', 'server')
		port	= cfg.get('database_mongodb', 'port')
		username	= cfg.get('database_mongodb', 'username')
		password	= cfg.get('database_mongodb', 'password')
		database	= cfg.get('database_mongodb', 'database')
		collection	= cfg.get('database_mongodb', 'collection')
		#database = "mnemosyne"
		#coll = "hpfeed"
		#server = "127.0.0.1"
		#log.msg(server)
		client = MongoClient("mongodb://{0}:{1}@{2}:{3}/{4}".format(username,password,server,int(port),database))
		db=client.get_default_database()
		self.fs=gridfs.GridFS(db)
		self.collection = db[collection]
		self.meta = {}

	# We have to return an unique ID
	def createSession(self, peerIP, peerPort, hostIP, hostPort):
		session = uuid.uuid4().hex
		self.meta[session] = {'session':session,'peerIP': peerIP, 'peerPort': peerPort, 
		'hostIP': hostIP, 'hostPort': hostPort, 'loggedin': None,
		'credentials':[], 'commands':[],"unknownCommands":[],'urls':[],'version': None, 'ttylog': None }
		return session

	def handleConnectionLost(self, session, args):
		log.msg('publishing metadata to mongodb')
		meta = self.meta[session]
		ttylog = self.ttylog(session)
		if ttylog: meta['ttylog'] = ttylog.encode('hex')
    		self.collection.insert(meta)

	def handleLoginFailed(self, session, args):
		u, p = args['username'], args['password']
		self.meta[session]['credentials'].append((u,p))

	def handleLoginSucceeded(self, session, args):
		u, p = args['username'], args['password']
		self.meta[session]['loggedin'] = (u,p)

	def handleCommand(self, session, args):
		c = args['input']
		self.meta[session]['commands'].append(c)
        
	def handleUnknownCommand(self, session, args):
		uc = args['input']
		self.meta[session]['unknownCommands'].append(uc)

	def handleInput(self, session, args):
		pass

	def handleTerminalSize(self, session, args):
		pass

	def handleClientVersion(self, session, args):
		v = args['version']
		self.meta[session]['version'] = v
		
	def handleFileDownload(self,session,args):
		url = args['url']
		self.meta[session]['urls'].append(url)


