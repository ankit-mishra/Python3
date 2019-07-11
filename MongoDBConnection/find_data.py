import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["users"]

#Find the first entry of the collection
x = mycol.find_one()
print(x)

#Find all the entries of the collection
for x in mycol.find():
    print(x)

print("Printing only the names and addresses, not the _ids")

#Return only the names and addresses, not the _ids
#First parameter in Find function is the QUERY
for x in mycol.find({}, {"_id": 0}):
    print(x)
