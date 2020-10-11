from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    # takes user to home page
    # ALL MAIN INFO HERE
    return render_template('home_page.html')


@app.route('/about')
def about_page():
    # takes user to about page
    # brief information of what this webapp is about with addition of images/animations
    return "this page will have information about what this site does"


@app.route('/lebron')
def lebron_page():
    # takes user to lebron page(to start off with, soon this will be players url if we advance
    # will contain image, name, height, age, ethnicity, hometown, salary,
    # teams
    return "this page will have general information about Lebron James"

@app.route('/lakers')
def lakers_page():
    # takes user to lakers page (soon to be teams page) containing the teams in their divisions
    # in alphabetical order with the year of its founding
    return "this page will have information on Lebron's current team: Lakers"


@app.route('/stats')
def stats_page():
    # takes user to stats page, here we will brainstorm a lot and see what happens
    return 'Stats'


@app.route('/trivia')
def trivia_page():
    # takes user to about page
    return "this page will have a 10 question trivia to see how much the user knows Lebron"
