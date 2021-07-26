from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired

class EncryptForm(FlaskForm):
    new_string = StringField("Text", validators=[DataRequired()])
    submit = SubmitField("Submit")