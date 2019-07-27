from pymongo import MongoClient
import datetime

class Logger:

    
    # initialize different collections
    def __init__(self,mongo): 

         
         self.user_coll = mongo.get_user_coll()
         self.log_coll = mongo.get_log_coll()
 
    #add log to the database
    def push_log(self,ID,bundle_name, project_name, log_text, log_time):
        
        log_date = datetime.datetime.now().strftime("%d/%m/%Y")
        n_log = {
                  "bundle_name": bundle_name,
                  "project_name": project_name,
                  "log_text": log_text,
                  "log_time": log_time,
                  "log_date": log_date
                }
        
        user = self.log_coll.find_one({'ID': ID})
        if user:
            self.log_coll.update_one({'ID': ID}, {'$push': {'logs': n_log}})
        else:
            n_log = {
                        "ID": ID,
                        "logs": [n_log]
                    }
            
            self.log_coll.insert_one(n_log)
            
    #returns log from the database
    def get_log(self, ID, bundle_name, project_name):
       
        log_list = list()
        user = self.log_coll.find_one({'ID': ID})
        if user:
            logs = user['logs']
            i=0
            for log in logs:
                
                if log['bundle_name'] == bundle_name and log['project_name'] == project_name:
                    i =i+1
                    n_log = {
                      "log_text": log['log_text'],
                      "log_time": log['log_time'],
                      "log_num": i,
                      "log_date": log['log_date']
                    }
                    log_list.append(n_log)
                
                    
        return log_list
        
    
    #returns user json from database
    def get_user(self, ID):
        
        user = self.user_coll.find_one({'ID': ID})
        return user
        




    