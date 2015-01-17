# Kippo_Mongodb
Mongodb support for Kippo honeypot

##Usage
* Run the script create.js to create the database,database user and collection

 `mongo create.js`


 you can edit create.js to change it's values

* copy the file **mongodb.py** to **< kippo-dir >/kippo/dblog** and you should be seeing kippo logging to mongodb

* get the logs from mongodb using mongoshell

 `use kippo`

 `db.log.find()`
