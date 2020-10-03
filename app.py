from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def homepage():
    """Show homepage for lunaTutor"""

    return render_template('home.html')


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
