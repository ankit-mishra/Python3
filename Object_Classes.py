class User:
    # Class Attributes
    name = "Test"
    
# The init() method is called the constructor and is always called when creating an object.
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print("Hello, my name is " + self.name)

user = User('Ankit Mishra')
user.sayHello()