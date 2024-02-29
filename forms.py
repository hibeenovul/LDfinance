from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class Registrationform(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20) ])
    email = StringField('Email address', validators=[InputRequired(), Email() ])
    phone = StringField('Phone number', validators=[InputRequired() ])
    password = PasswordField('Password', validators=[InputRequired() ])
    confirmm_password = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password') ])
    submit = SubmitField('Sign up')

class Loginform(FlaskForm):
    email = StringField('Email address', validators=[InputRequired(), Email() ])
    password = PasswordField('Password', validators=[InputRequired() ])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')