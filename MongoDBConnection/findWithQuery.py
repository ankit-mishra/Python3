import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["users"]

myquery = {"address": "Lowstreet 27"}

mydata = mycol.find(myquery)

for x in mydata:
    print(x)

print("Going to print advanced query result: $gt is greater than modifier")

#Find documents where the address starts with the letter "S" or higher
#Advanced Query
myquery = {"address": {"$gt": "S"}}

mydata = mycol.find(myquery)

for x in mydata:
    print(x)


print("Going to print advanced query result with regular expression")

#Find documents where the address starts with the letter "S"
#With Regular expression
myquery = {"address": {"$regex": "^S"}}

mydata = mycol.find(myquery)

for x in mydata:
    print(x)
