from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from bundle import Bundle
from mongo import Mongo


class LogForm(FlaskForm):
    
    
    b_field = SelectField("Bundle: ", choices=Bundle(Mongo()).get_bundle_names(), default=1)
    
    p_field = SelectField("Project: ", choices=[("Project","Project")], default=1)
    
    i_field = SelectField("ID: ", choices=[("ID","ID")], default=1)
    
    log_text = TextAreaField('log_text',
                         validators=[DataRequired(), Length(min=10, max=1000)])
        
    log_time = StringField('log_time',
                           validators=[DataRequired(), Length(min=1, max=5)])
    

    
    submit = SubmitField('Submit')
    
    

    