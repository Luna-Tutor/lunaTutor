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


