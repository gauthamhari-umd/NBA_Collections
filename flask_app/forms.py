from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField,SelectField,IntegerField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)


from .models import User


class SearchForm(FlaskForm):
    search_query = StringField(
        "Query", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Search")


class ChooseCollectionForm(FlaskForm):
    submit = SubmitField("Submit")
    text = TextAreaField('Name')
    collection = SelectField('Select Collection', choices=["1","2","3"], coerce=str)

class CreateCollectionForm(FlaskForm):
    submit = SubmitField("Create Collection")
    name = StringField(
        "Name of Collection", validators=[InputRequired(), Length(min=1, max=40)]
    )
    size = IntegerField(
        "Size"
    )

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")


# TODO: implement fields
class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired()]
    )
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")


# TODO: implement
class UpdateUsernameForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    submit_username = SubmitField("Update Username") 
    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")


# TODO: implement
class UpdateProfilePicForm(FlaskForm):
    picture = FileField("Picture", validators=[FileRequired(), FileAllowed(["jpg", "png"])]
    )    
    submit_picture = SubmitField("Update Picture") 
