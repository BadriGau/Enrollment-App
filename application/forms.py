from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = StringField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = StringField("Password",validators=[DataRequired()])
    password_confirm = StringField("Confirm Password",validators=[DataRequired()])
    first_name = StringField("First Name",validators=[DataRequired()])
    last_name = StringField("Last Name",validators=[DataRequired()])
    submit = SubmitField("Login")
    