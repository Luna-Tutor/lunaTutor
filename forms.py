from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length

SUBJECT_LIST = ['Biology', 'Physics', 'Chemistry']


class SignUpForm(FlaskForm):
    """Signup Form"""

    username = StringField('Name', validators=[
        DataRequired()
        ])
    email = StringField('Email', validators=[
        Email(message=('Not a valid email address.')),
        DataRequired()
        ])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=6, message=('Password needs to be 6 or more characters!'))
        ])
    first_name = StringField('First Name', validators=[
        DataRequired()
        ])
    last_name = StringField('Last Name', validators=[
        DataRequired()
        ])

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('Name', validators=[
        DataRequired()
        ])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=6, message=('Password needs to be 6 or more characters!'))
        ])

class QuestionForm(FlaskForm):
    """Ask Question"""

    subject = SelectField('Subject', choices=SUBJECT_LIST, validators=[
        DataRequired(),
        ])
    title = StringField('Title', validators=[
        DataRequired()
        ])
    hashtag = StringField('Hashtag')
    details = StringField('Details', validators=[
        DataRequired(),
        Length(min=1, message=('Please fill in the details.'))
        ])

class AnswerForm(FlaskForm):
    """Answer"""

    answer = TextAreaField('Answer', validators=[
      DataRequired()
    ])