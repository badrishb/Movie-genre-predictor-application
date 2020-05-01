from wtforms import TextField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm
class homef(FlaskForm):
    photo = FileField("Upload photograph",validators=[FileRequired()])
    submit = SubmitField('Submit')