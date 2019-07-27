class Bundle:
    
    #initializes different collections in the database
    def __init__(self, mongo): 
  
         self.bundle_coll = mongo.get_bundle_coll()
         self.user_coll = mongo.get_user_coll()
         self.log_coll = mongo.get_log_coll()
         
         self.bundles_jlst = list(self.bundle_coll.find())
         self.users_jlst = list(self.user_coll.find())
    
 
    # return bundle_names for dropdown list
    def get_bundle_names(self):
        
        bundle_lst = list()
        
        for bundle in self.bundles_jlst:
            bundle_lst.append(bundle["bundle_name"])
    
        return [('',"Select a Bundle")] + [(b,b) for b in bundle_lst]
    
    # return project_name for dropdown list
    def get_project_names(self,bundle_name):
        
        project_lst = list()
        
        for bundle in self.bundles_jlst:
            if bundle["bundle_name"] == bundle_name:
                for project in bundle["projects"]:
                    project_lst.append(project["project_name"])
                break
            
        
        p_db = []

        for p in project_lst:
            p_ob = {}
            p_ob['name']=p
            p_db.append(p_ob)
    
        return  [{'name': 'Select a Project'}] + p_db
    
    
    # return IDs for dropdown list
    def get_IDs(self,bundle_name,project_name):
        
        ID_lst = list()
        
        for bundle in self.bundles_jlst:
            if bundle["bundle_name"] == bundle_name:
                for project in bundle["projects"]:
                    if project["project_name"] == project_name:
                        for ID in project["IDs"]:
                            ID_lst.append(ID["ID"])
                        break
                break
        
    
        i_db = []

        for i in ID_lst:
            i_ob = {}
            i_ob['name']=i
            i_db.append(i_ob)
    
        return i_db
    
    #return all the registered IDs for add_project
    def get_ID_list(self):
        
        ID_lst = list()
        
        for user in self.users_jlst:
            if user["ID"] != "admin": 
                ID_lst.append(user["ID"])
        
        return ID_lst
        
    #return all the registered bundles for add_project
    def get_bundle_list(self):
        
        bundle_lst = list()
        
        for bundle in self.bundles_jlst:
            bundle_lst.append(bundle["bundle_name"])
        
        return bundle_lst
    
    #return all the registered projects for add_project
    def get_project_list(self):
        
        project_lst = list()
        
        for bundle in self.bundles_jlst:
            for project in bundle["projects"]:
                project_lst.append(project["project_name"])
    
        return  project_lst
    
    #adds project to the database
    def add_project(self,n_bundle, n_project, n_ID):
        
    
        id_dict = {'ID': n_ID}
        project_dict = {"project_name": n_project, "IDs": [ id_dict] }
        bundle_dict = {"bundle_name": n_bundle, "projects": [ project_dict ] }
        b_flag = 0
        p_flag = 0
        
        for bundle in self.bundles_jlst:
            if bundle["bundle_name"] == n_bundle:
                b_flag = 1
                for project in bundle["projects"]:
                    if project["project_name"] == n_project:
                        p_flag = 1
                        for ID in project["IDs"]:
                            if ID["ID"] == n_ID:
                                return -1
                            
                        self.bundle_coll.update_one({"bundle_name": n_bundle , "projects.project_name": n_project },{'$push': {'projects.$.IDs': id_dict }} )
                        return 1
                    
                if p_flag == 0:
                    self.bundle_coll.update_one({"bundle_name": n_bundle}, {'$push': {'projects': project_dict }} )
                    return 1
                
        if b_flag == 0:
            self.bundle_coll.insert_one(bundle_dict)
            return 1
        
        





    