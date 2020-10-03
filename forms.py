import wtforms
from wtforms import StringField, TextField, SubmitField, SelectField
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
    password = StringField('Password', validators=[
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
    password = StringField('Password', validators=[
        DataRequired(), 
        Length(min=6, message=('Password needs to be 6 or more characters!'))
        ])

class QuestionForm(FlaskForm):
    """Ask Question"""

    subject = SelectField('Subject', validators=[
        DataRequired(),
        choices=SUBJECT_LIST
        ])
    title = StringField('Title', validators=[
        DataRequired()
        ])
    details = StringField('Details', validators=[
        DataRequired(),
        Length(min=1, message=('Please fill in the details.'))
        ])

class AnswerForm(FlaskForm):
    """Answer"""

    answer = StringField('Answer', validators=[
      DataRequired()
    ])