from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=6,max=15)])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password",validators=[DataRequired(),Length(min=6,max=15),EqualTo(password)])
    first_name = StringField("First Name",validators=[DataRequired(),Length(min=3,max=50)])
    last_name = StringField("Last Name",validators=[DataRequired(),Length(min=3,max=50)])
    submit = SubmitField("Login")
    
    
    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Use another one")