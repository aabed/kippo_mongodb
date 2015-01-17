new Mongo()
conn= new Mongo()
db= conn.getDB("kippo")

/*db.createUser(
  {
    user: "kippo",
    pwd: "kippo_pass",
    roles: [ { role: "userAdmin", db: "kippo" } ]
  }
)*/
db.createCollection("log")
