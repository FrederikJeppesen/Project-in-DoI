#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField, widgets
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class CustomerLoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
    signIn = SubmitField('Sign in')

class RestaurantLoginForm(FlaskForm):
    id = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Base', validators=[DataRequired()])
    submit = SubmitField('Log in')

class CourierLoginForm(FlaskForm):
    id = StringField('Courier id', validators=[DataRequired()])
    password = PasswordField('Base', validators=[DataRequired()])
    submit = SubmitField('Log in')

class AddCustomerForm(FlaskForm):
    base = StringField('Base',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    zone = IntegerField('Zone',
                        validators=[DataRequired()])
    submit = SubmitField('Add')

class AddFoodForm(FlaskForm):
    choice = RadioField('Choose your meal - you can only select one:', choices=[])
    takeout = BooleanField()
    submit = SubmitField('Add')
