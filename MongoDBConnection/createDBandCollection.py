import pymongo

#Creating Database instance
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Creating Database
mydb = myclient["myPyDatabase"]

#Creating collection
mycol = mydb["customers"]

#Creating data object to be inserted"
mydist = {"name": "Manas", "address": "Sopra Steria"}

#Insert single entry in the collection
x = mycol.insert_one(mydist)

print(x.inserted_id)

dblist = myclient.list_database_names()
print(dblist)
if "myPyDatabase" in dblist:
  print("The database exists.")
else:
  print("myPyDatabase does not exist")

mycol = mydb["customers"]
collist = mydb.list_collection_names()
print(collist)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

#Insert many entries
y = mycol.insert_many(mylist)

#Here inserted_idS holds the ids of the inserted documents.
print(y.inserted_ids)

#Creating new collection in the same DB
myUserCol = mydb["users"]

#Data with custom _id (i.e. _id is not assigned by MongoDB)
mylistwithId = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

z = myUserCol.insert_many(mylistwithId)

print(z.inserted_ids)
