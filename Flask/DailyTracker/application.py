from flask import Flask, render_template, flash, redirect, url_for, request, session
from forms import Registration, Login
from flask_wtf import FlaskForm
from pymongo import MongoClient
import bcrypt
#from wtforms import SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f50ee8ef32aff7f77d08d536d00e1bd'

client = MongoClient('mongodb://localhost:27017/')

db = client['DailyLogs']
user_coll = db['users']
projects_coll = db['bundles']


class Form(FlaskForm):
    project = ["project 1", "project 2"]
    person = ["person 1", "person 2"]
    
    
    
    
@app.route("/log", methods=['GET', 'POST'])
def log():
    form = Form()
    return render_template('log.html', form=form)






@app.route("/view", methods=['GET', 'POST'])
def view():
    form = Form()
    
    return render_template('view.html', form=form)









@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
#        if form.email.data == "admin@log.com" and form.password.data == "password":
#            flash("You have been logged in!", 'success')
#            return redirect(url_for('view'))
#        else:
#            flash('Login Unsuccessful. Check Email or Password', 'danger')
        users = user_coll
        login_user = users.find_one({'ID': request.form['ID']})
        
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['ID'] = request.form['ID']
                flash(f'Welcome {form.ID.data}!','success')
                return redirect(url_for('log'))
            
        flash(f'Invalid ID/Password!','danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', title='Login', form=form)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    
    if form.validate_on_submit():
        users = user_coll
        existing_user = users.find_one({'ID': request.form['ID']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'ID': request.form['ID'], 'password': hashpass})
            session['ID'] = request.form['ID']
            flash(f'Account created for {form.ID.data}!','success')
            return redirect(url_for('log'))
        
        flash(f'{form.ID.data} is Already Registered!','danger')
        return redirect(url_for('login'))
            

    
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
