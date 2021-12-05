from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TossingForm(FlaskForm):
    coin1 = SelectField(choices = ['Head','Tail'])
    coin2 = SelectField(choices=['Head', 'Tail'])
    coin3 = SelectField(choices=['Head', 'Tail'])
    submit = SubmitField("Submit")