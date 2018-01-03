from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class UpdatePizza(FlaskForm):
    name = TextAreaField('Name of the Pizza', validators=[Required()])
    price = TextAreaField('Price', validators=[Required()])
    photo = FileField(validators=[Required()])
    submit = SubmitField('SUBMIT')
