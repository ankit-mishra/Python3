from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddProjectForm(FlaskForm):
    
    
    bundle_text = StringField('Bundle',
                         validators=[DataRequired()])
        
    project_text = StringField('Project',
                           validators=[DataRequired()])
    
    ID_text = StringField('ID',
                           validators=[DataRequired()])
 
    submit = SubmitField('Add')
    

    