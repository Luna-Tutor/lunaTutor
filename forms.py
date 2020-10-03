import wtforms
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

SUBJECT_LIST = ['Biology', 'Physics', 'Chemistry']


class SignUpForm(wtforms.Form):
    """Signup Form"""

    username = StringField('Name', [
        DataRequired()
        ])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()
        ])
    password = StringField('Password', [
        DataRequired(), 
        Length(min=6, message=('Password needs to be 6 or more characters!'))
        ])
    first_name = StringField('First Name', [
        DataRequired()
        ])
    last_name = StringField('Last Name', [
        DataRequired()
        ])

class LoginForm(wtforms.Form):
    """Login Form"""

    username = StringField('Name', [
        DataRequired()
        ])
    password = StringField('Password', [
        DataRequired(), 
        Length(min=6, message=('Password needs to be 6 or more characters!'))
        ])

class QuestionForm(wtforms.Form):
    """Ask Question"""

    subject = SelectField('Subject', [
        DataRequired(),
        choices=SUBJECT_LIST
        ])
    title = StringField('Title', [
        DataRequired()
        ])
    details = StringField('Details', [
        DataRequired(),
        Length(min=1, message=('Please fill in the details.'))
        ])

class AnswerForm(wtforms.Form):
    """Answer"""

    answer = StringField('Answer', [
      DataRequired()
    ])