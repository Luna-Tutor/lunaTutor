""" Seed file to make sample data for db. """

from models import db, Subject, User, Question, Answer
from app import app

# Create all tables
db.drop_all()
db.create_all()

# 1st create our data
# python seed.py

biology = Subject(
    id=1,
    name="Biology"
)

chemistry = Subject(
    id=2,
    name="Chemistry"
)

physics = Subject(
    id=3,
    name="Physics"
)

astronomy = Subject(
    id=4,
    name="Astronomy"
)

db.session.add_all([biology, chemistry, physics, astronomy])
db.session.commit()
