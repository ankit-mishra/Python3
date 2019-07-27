Libraries Imported

pymongo  - for MongoDB
flask - for running server 
wtforms - for HTML Forms
bcrypt - for Password Hashing
flask_login - for Login Manager

installation...

pip install pymongo
pip install flask
pip install wtforms
pip install bcrypt
pip install flask-login

Running the application...
	1) start mongoDb:
		net start MongoDb

	2) start server:
		python run.py

Application Setup

Home page/ Login page:
	http://127.0.0.1:5000/

1) Make an admin account, Login and add project data.
by default, Registration ID for admin account is 'admin' (use this while creating account),
you can change it by updating 'admin_id' field in strings.py 

2) Register individual IDs (Users).

3) Now individual users can add logs to the assigned projects.

4) Now Admin account can be used to view Logs and add more project data.

