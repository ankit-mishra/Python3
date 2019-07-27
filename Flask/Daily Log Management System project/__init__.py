from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from forms import Registration, Login
import bcrypt
from bundle import Bundle
from log_form import LogForm
from logger import Logger
from view_form import ViewForm
from add_project import AddProjectForm
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from bson.objectid import ObjectId
from user import User
from mongo import Mongo
from strings import SECRET_KEY, admin_id

#initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


#initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#initialize Mongo class
mongo = Mongo()
user_coll = mongo.get_user_coll()


#initialize Mongo class

bundle = Bundle(mongo)


#load current user
@login_manager.user_loader
def load_user(user_id):
    
    user_json = user_coll.find_one({'_id': ObjectId(user_id)})
    return User(user_json)
    

#Daily Log page
@app.route("/", methods=['GET', 'POST'])
@app.route("/log", methods=['GET', 'POST'])
@login_required
def log():
    
    logger = Logger(mongo)
    
    if current_user.ID == admin_id: 
        flash(f'This account is not authorised to log!','danger')
        return redirect(url_for('view'))
    else:
        form = LogForm()
        if request.method == 'POST':
            
            if current_user.ID == form.i_field.data:
                logger.push_log(form.i_field.data, form.b_field.data, form.p_field.data, form.log_text.data, form.log_time.data)
                flash(f'{form.i_field.data} successfully logged todays work!','success')
                 
            else:
                flash(f'You can Log only your progress!','danger')
                return redirect(url_for('log'))
#        
        return render_template('log.html', form=form, user=current_user)




#view Log page
@app.route("/view", methods=['GET', 'POST'])
@login_required
def view():
    
    logger = Logger(mongo)
    global bundle 
    bundle = Bundle(mongo)
    
    if current_user.ID != admin_id:
        flash(f'This account is not authorised to view logs!','danger')
        return redirect(url_for('log'))
    else:
        form = ViewForm()
        if request.method == 'POST':
            log_list = logger.get_log(form.i_field.data, form.b_field.data, form.p_field.data)
            user_json = logger.get_user(form.i_field.data)
            if user_json:
                user = User(user_json)
                if log_list == []:
                    return render_template('view.html', form=form, no_log="Currently no existing Logs to view", user=user)
                else:
                    return render_template('view.html', form=form, log_list=log_list, user=user)
            else:
                flash(f'User does not Exist!','danger')
                return redirect(url_for('view'))
        
        return render_template('view.html', form=form)



#Dependent drop down
@app.route('/project/<bundle_name>')
@login_required
def project(bundle_name):
    projects = bundle.get_project_names(bundle_name)
    
    return jsonify({'projects': projects})


#Dependent drop down
@app.route('/id/<bundle_name>/<project_name>')
@login_required
def ID(bundle_name, project_name):
    print(bundle_name,project_name)
    IDs = bundle.get_IDs(bundle_name, project_name)
    
    return jsonify({'IDs': IDs})



#login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():

        l_user = user_coll.find_one({'ID': request.form['ID']})
        
        
        if l_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), l_user['password']) == l_user['password']:
                loginuser = User(l_user)
                login_user(loginuser, remember=False)
                flash(f'Welcome {form.ID.data}!','success')
                
                if current_user.ID == admin_id:
                    return redirect(url_for('view'))
                else:
                    return redirect(url_for('log'))
            
        flash(f'Invalid ID/Password!','danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', title='Login', form=form)


#register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    
    if form.validate_on_submit():
        existing_user = user_coll.find_one({'ID': request.form['ID']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt())
            user_coll.insert({'ID': request.form['ID'], 'password': hashpass, 'name':request.form['name'] , 'email':request.form['email']})
            flash(f'Account created for {form.ID.data}!','success')
            return redirect(url_for('log'))
        
        flash(f'{form.ID.data} is Already Registered!','danger')
        return redirect(url_for('login'))
            

    
    return render_template('register.html', title='Register', form=form)


#logut route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


#add project route
@app.route("/add_projects", methods=['GET', 'POST'])
@login_required
def add_projects():

    bundle = Bundle(mongo)
    if current_user.ID != admin_id:
        flash(f'This account is not authorised to add Projects!','danger')
        return redirect(url_for('log'))
    else:
        f = 0
        form = AddProjectForm()
        bundle_lst = bundle.get_bundle_list()
        project_lst = bundle.get_project_list()
        ID_lst = bundle.get_ID_list()
        if request.method == 'POST':
            f = bundle.add_project(form.bundle_text.data, form.project_text.data, form.ID_text.data)
            if f == -1:
                flash(f'Already Exists!','danger')
                redirect(url_for('add_projects'))
            elif f == 1:
                flash(f'Successfully Added!','success')
                redirect(url_for('add_projects'))

        
        return render_template('add_projects.html', form=form, bundle_lst=bundle_lst, project_lst=project_lst, ID_lst=ID_lst )

