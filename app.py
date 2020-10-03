from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



# landing page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    """Show homepage for lunaTutor"""

    return render_template('home.html')

# homepage for authenticated users (or is this the same as landing page?)


# login route


# sign up route

            

# Question and answer routes 
# What do the routes look like if taking an AJAX approach?
# It may be simpler to just create a route for each subject and question
# ex) www.lunatutor.com/biology  ->  page showing all biology questions
# ex) www.lunatotor.com/chemistry/23  ->  page showing question and answers for question No.23



# GENERAL ROUTES FOR BOARDS
@app.route('/q', methods=['GET', 'POST'])
def feedpage():
    """Show general feed for posted questions """

    return render_template('/board/feed.html')


@app.route('/q/biology', methods=['GET', 'POST'])
def biologyBoard():
    """Show question board for biology related questions """

    return render_template('board.html')


@app.route('/q/chemistry', methods=['GET', 'POST'])
def chemistryBoard():
    """Show question board for chemistry related questions  """

    return render_template('board.html')


@app.route('/q/physics', methods=['GET', 'POST'])
def physicsBoard():
    """Show question board for physics related questions  """

    return render_template('board.html')
