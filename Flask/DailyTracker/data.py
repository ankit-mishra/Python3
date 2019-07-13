from pymongo import MongoClient
from json import loads, dumps
from strings import mongo_lnk,db_name

class User:
    

    # establish mongoDB connection and initialize database 
    def __init__(self): 
        
         self.client = MongoClient(mongo_lnk)
         self.db = self.client[db_name]
         
         
     
     
     def project():
         return 0
    
    def jsonify():
        return 0
    
    def add_project():
        return 0
    
    
 
    def read_data(self,xml_data):
        
        json_data = loads(dumps(xml_data))
        collection_name = list(json_data.keys())[0]
        
        
        #inserting data
        self.collection.insert_one(xml_data[collection_name])
        



    
    #import data from mongoDB database and return json
    def readMongoDB(self):
        
        collection_json =  list(self.collection.find())
        collection_json = collection_json[0]
        collection_json.pop('_id')
        return collection_json
        


