# Kippo_Mongodb
Mongodb support for Kippo honeypot

##Usage
* Run the script create.js to create the database,database user and collection

 `mongo create.js`


 you can edit create.js to change it's values

* copy the file **mongodb.py** to **< kippo-dir >/kippo/dblog** and you should be seeing kippo logging to mongodb

* add those lines to the end of the **kippo.cfg** file

> [database___mongodb]
<br>server = 127.0.0.1
<br>port = 27017
<br>username = kippo
<br>password = kippo_pass
<br>database = kippo
<br>collection = log 

* get the logs from mongodb using mongoshell

 `use kippo`

 `db.log.find()`

##Inspired by and based on
* [Hpfeeds] 
[Hpfeeds]:https://github.com/rep/hpfeeds/blob/master/appsupport/kippo/hpfeeds.py

