from flask import Flask, render_template, request, redirect, session, flash, g
from models import connect_db, db, User, Question, Answer, Subject, Tag
from forms import LoginForm, SignUpForm, AnswerForm, QuestionForm
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "abc123"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgres:///luna_db')

connect_db(app)


CURR_USER_KEY = 'user'


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""
    # This function runs before every request that is made.

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


# landing page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    """Show homepage for lunaTutor"""

    return render_template('home.html')

# homepage for authenticated users (or is this the same as landing page?)


# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ show login page if GET / handle login if POST """
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/q")

        flash("Invalid credentials.", 'danger')

    return render_template('userLoginSignupForm/login.html', form=form)


# sign up route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ show signup page with form if GET / handle signup if POST """
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # check for existing user
            existing_user = User.query.filter_by(email=form.email.data)

            if existing_user is None:
                user = User.register(
                    username=form.username.data,
                    password=form.password.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data
                )
            db.session.add(user)
            db.session.commit()

            do_login(user)
            return redirect("/q")

        # if existing_user if true:
        flash('A user with that email exists.')
        return redirect('/signup')
    # GET: render signup form
    return render_template('userLoginSignupForm/signup.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash(f"Successfully logged out", 'success')
    return redirect('/login')


# feed route
@app.route('/q', methods=['GET'])
def show_question_feed():
    """ show the question feed across all subjects """

    questions = Question.query.all()

    hashtags = Tag.query.all()

    return render_template('/board/feed.html', questions=questions, hashtags=hashtags, user=g.user)


# subject feed route
@app.route("/q/<subject>", methods=['GET'])
def show_subject_questions(subject):
    """ show subject-specific questions """
    questions = db.session.query(Question).filter(subject == subject).all()

    return render_template('board/feed.html', questions=questions)


@app.route("/q/ask", methods=['GET', 'POST'])
def post_question():
    """Post a question"""

    form = QuestionForm()

    if request.method == 'POST':

        if not g.user:
            return redirect('/login')
        if form.validate_on_submit():
            question = Question.post(
                subject=form.subject.data,
                title=form.title.data,
                content=form.content.data,
                hashtag=form.hashtag.data
            )
            db.session.add(question)
            db.session.commit()

            return redirect(f'/q/{question.subject}')

    return render_template('board/ask.html', form=form)


@app.route('/q/<subject>/<int:qid>', methods=['GET', 'POST'])
def question_detail_page(qid):
    """ Show detail on question and all answers / if Post, handle answer """
    form = AnswerForm()

    question = Question.query.get_or_404(qid)

    if form.validate_on_submit():
        # handle answer form
        answer = Answer.post(
            answer=form.answer.data
        )
        db.session.add(answer)
        db.session.commit()

        return redirect(f'/q/{question.subject}/{qid}')

    return render_template('board/question-detail.html', question=question, form=form)

# About Page route
@app.route('/about', methods=['GET'])
def about():
    """Load about page for the project"""

    return render_template('about')

# Question and answer routes
# What do the routes look like if taking an AJAX approach?
# It may be simpler to just create a route for each subject and question
# ex) www.lunatutor.com/biology  ->  page showing all biology questions
# ex) www.lunatotor.com/chemistry/23  ->  page showing question and answers for question No.23
