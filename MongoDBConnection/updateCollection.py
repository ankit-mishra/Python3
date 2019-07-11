import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["users"]

#Update one document in the collection
myquery = {"address": "Apple st 652"}
newvalue = {"$set": {"address" : "Sopra Steria"}}

mycol.update_one(myquery, newvalue)

for x in mycol.find():
    print(x)


#Update many documents in the collection
myquery = {"address": {"$regex": "^S"}}
newvalue = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalue)

print(x.modified_count, "documents updated")

print("Docs with name Minnie:")
#Find document with name Minniw
myquery = {"name": "Minnie"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

