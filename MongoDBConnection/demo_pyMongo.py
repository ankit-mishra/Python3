import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['myPyDatabase']

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "myPyDatabase" in dblist:
  print("The database exists.")
else:
  print("myPyDatabase does not exist")


mycol = mydb["customers"]
collist = mydb.list_collection_names()
print(collist)

if "customers" in collist:
  print("The collection exists.")
else:
  print("The collection does not exists.")  
