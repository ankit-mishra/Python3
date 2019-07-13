from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Registration(FlaskForm):
    
    
    ID = StringField('ID',
                         validators=[DataRequired(), Length(min=2, max=20)])
        
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_pass = PasswordField('REPassword', validators=[DataRequired(), EqualTo('password')])
    

    
    submit = SubmitField('Register')
    
    
class Login(FlaskForm):
    
    ID = StringField('ID',
                         validators=[DataRequired(), Length(min=2, max=20)])
    
    password = PasswordField('Password', validators=[DataRequired()])
  

    
    submit = SubmitField('Login')
    