from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from bundle import Bundle
from mongo import Mongo

class ViewForm(FlaskForm):
    
    
    b_field = SelectField("Bundle: ", choices=Bundle(Mongo()).get_bundle_names(), default=1)
    
    p_field = SelectField("Project: ", choices=[("Project","Project")], default=1)
    
    i_field = SelectField("ID: ", choices=[("ID","ID")], default=1)
    
    submit = SubmitField('Submit')
    
    

    