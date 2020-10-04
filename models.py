""" SQLAlchemy models for LunarTutor App"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """ Connect to database """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Question Model"""
    __tablename__="users"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    username = db.Column(db.String(20),
                   nullable = False,
                   unique = True)

    password = db.Column(db.Text,
                   nullable = False)

    first_name = db.Column(db.String(15),
                   nullable = False)

    last_name = db.Column(db.String(15),
                   nullable = False)
    email = db.Column(db.String(30),
                   nullable = False)
    
    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        
        # 
        hashed = bcrypt.generate_password_hash(password)

        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")
        
        # returns user instance of user with hashed password
        return cls(username=username, password=hashed_utf8, email= email, first_name=first_name, last_name=last_name)
    
    @classmethod
    def authenticate(cls, username, password):
        """ Validates that user exists in db & password is correct. Returns user instance if authenticated or False if not"""

        found_user = User.query.filter_by(username=username).first()

        if found_user and bcrypt.check_password_hash(found_user.password, password):
            return found_user
        else :
            return False      

class Question(db.Model):
    """Question Model"""
    __tablename__="questions"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(70),
                      nullable=False)
    content = db.Column(db.String(500),
                      nullable=False,
                      unique=True)
    subjectID = db.Column(db.Integer,
                db.ForeignKey("subjects.id"))
    
    authorID =  db.Column(db.Integer,
                db.ForeignKey("users.id"))
       
    date = db.Column(db.String(50),
                   nullable=False,
                   default=datetime.utcnow())
    answered = db.Column(db.Boolean,
                   nullable=False,
                   default=False)

    subject = db.relationship("Subject", backref="questions")

    author = db.relationship("User", backref="questions")

    
class Subject(db.Model):
    """Subject Model"""
    
    __tablename__="subjects"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)


class Answer(db.Model):
    """Answer Model"""
    
    __tablename__="answers"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    authorID =  db.Column(db.Integer,
                db.ForeignKey("users.id"))
    
    questionID = db.Column(db.Integer,
                 db.ForeignKey("questions.id"))

    content= db.Column(db.String(700),
                       nullable=False)

    date = db.Column(db.String(20),
                   nullable=False,
                   default=datetime.utcnow())
    upvotes = db.Column(db.Integer)
    
    question = db.relationship("Question", backref="answers")

    author = db.relationship("User", backref="users")



class QuestionTag(db.Model):
    """Question Model"""
    
    __tablename__="questionstags"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)    
    questionID =  db.Column(db.Integer,
                  db.ForeignKey("questions.id"))
    tagID = db.Column(db.Integer,
            db.ForeignKey("tags.id"))
            
class Tag(db.Model):
    """Tag Model"""
    __tablename__="tags"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)       
    name = db.Column(db.String(20),
                   nullable=False)




