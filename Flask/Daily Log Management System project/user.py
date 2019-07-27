from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_json):
        self.user = user_json
        self.ID = user_json['ID']
        self.password = user_json['password']
        self.email = user_json['email']
        self.name = user_json['name']
        
    def get_id(self):
        object_id = self.user.get('_id')
        return str(object_id)