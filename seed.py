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


# q1 = Question(
#     id=11,
#     title="What is an atom?",
#     content="Yeah so what is an atom????",
#     subjectID=2,
#     authorID=11,
#     hashtag="atom",
#     date="Oct3",
#     answered=False
# )

# q2 = Question(
#     id=12,
#     title="Why are planets round?",
#     content="Why are all the planets the same shape?",
#     subjectID=4,
#     authorID=12,
#     hashtag="planets",
#     date="Oct 2",
#     answered=True
# )

# db.session.add_all([q1, q2])
# db.session.commit()


# a1 = Answer(
#     id=1, 
#     authorID=13,
#     questionID=1,
#     content="An atom is the smalles unit of matter",
#     date="Oct 3",
#     upvotes= 5
# )

# a2 = Answer(
#     id=2,
#     authorID=14,
#     questionID=2,
#     content="A planet is that shape because of gravity",
#     date="Oct 3",
#     upvotes=10
# )

# db.session.add_all([a1, a2])
# db.session.commit()
