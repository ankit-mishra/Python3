from pymongo import MongoClient
from strings import mongo_lnk, db_name, bundle_coll_name, log_coll_name, user_coll_name 


class Mongo:
    def __init__(self): 
        
         self.client = MongoClient(mongo_lnk)
         self.db = self.client[db_name] 

         
    def get_bundle_coll(self):
        return self.db[bundle_coll_name]
    
    def get_log_coll(self):
        return self.db[log_coll_name]
    
    def get_user_coll(self):
        return self.db[user_coll_name]
    
