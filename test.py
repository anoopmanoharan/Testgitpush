import pymongo

client = pymongo.MongoClient("mongodb+srv://anoopmanoharan:Idontremember@cluster0.nibrjix.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

c = {
    "name": "anoop",
   "email": "anoopmanoharan2@gmail.com",
   "surname": "manoharan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(c)

