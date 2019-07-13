from pymongo import MongoClient
from json import loads, dumps
from strings import mongo_lnk,db_name

class MongoDB:
    

    # establish mongoDB connection and initialize database 
    def __init__(self): 
        
         self.client = MongoClient(mongo_lnk)
         self.db = self.client[db_name]
         
          
    #export xml data to mongoDB database 
    def writeMongoDB(self,xml_data):
        
        json_data = loads(dumps(xml_data))
        collection_name = list(json_data.keys())[0]
        
        # make a collection in the database
        self.collection = self.db[collection_name]
        
        #clear any previous data
        self.collection.delete_many({})
        
        #inserting data
        self.collection.insert_one(xml_data[collection_name])

    
    #import data from mongoDB database and return json
    def readMongoDB(self):
        
        collection_json =  list(self.collection.find())
        collection_json = collection_json[0]
        collection_json.pop('_id')
        return collection_json
        


