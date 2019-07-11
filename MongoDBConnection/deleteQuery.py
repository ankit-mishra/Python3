import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)


#Delete all documents were the address starts with the letter S
myquery = {"address" : {"$regex": "^O"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted")


#Delete all documents
x = mycol.delete_many({})

print(x.deleted_count, "documents deleted")


#Drop collection
mycol.drop()
