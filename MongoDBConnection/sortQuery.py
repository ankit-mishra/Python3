import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myPyDatabase"]
mycol = mydb["users"]

#Sort in ascending order
mydata = mycol.find().sort("name")

for x in mydata:
    print(x)

print("Going to print in Descending order")

#Sort in descending order
mydata = mycol.find().sort("name", -1)

for x in mydata:
    print(x)
