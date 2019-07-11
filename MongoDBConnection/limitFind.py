import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["users"]

mydoc = mycol.find()

for x in mydoc:
    print(x)

#Limit the result to only return 5 documents
print("Printing only 5 documents")

mydoc = mycol.find().limit(5)

for x in mydoc:
    print(x)
