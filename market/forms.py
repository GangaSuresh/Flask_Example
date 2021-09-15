from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User


class RegisterForm(FlaskForm): #checks with the name validate_username , built in names , try same pattern with any like validate_email etc
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exist! Please try a different username")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')


    username=StringField(label='User Name:',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='Email Address: ',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password: ',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='User Name:',validators=[DataRequired()])
    password=PasswordField(label='Password: ',validators=[DataRequired()])
    submit=SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')

class mlForm(FlaskForm):
    years=FloatField(label='Years of experience: ',validators=[DataRequired()])
    submit = SubmitField(label='Predict salary')