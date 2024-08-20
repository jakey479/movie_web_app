from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AccountAccessForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=5, max=20), ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)]) 
    submit = SubmitField('Sign In')

class LoginForm(AccountAccessForm):
    # value of remember_me will be passed to flask_login's login_user function to determine whether to persist the user's session acrosss browser restarts
    remember_me = BooleanField('Remember Me')

class RegistrationForm(AccountAccessForm):
    # the class variables will define the fields of the form
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match'), ])
    birthday = StringField('Birthday', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=50)])
    occupation = StringField('Occupation', validators=[DataRequired()])
    address =StringField('Address', validators=[DataRequired()])
