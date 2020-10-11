from flask import Flask, render_template
from stats.stats import PlayerStats
import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    # takes user to home page
    # ALL MAIN INFO HERE
    return render_template('home_page.html')


@app.route('/lebron')
def lebron_page():
    # takes user to lebron page(to start off with, soon this will be players url if we advance
    # will contain image, name, height, age, ethnicity, hometown, salary,
    # teams
    return render_template('lebron_page.html')


@app.route('/lakers')
def lakers_page():
    # takes user to lakers page (soon to be teams page) containing the teams in their divisions
    # in alphabetical order with the year of its founding
    return render_template('lakers_page.html')


@app.route('/stats/<date>')
def stats_page(date):
    split_date = [int(x) for x in date.split('-')]
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

    lbj = PlayerStats('jamesle01')

    stats = lbj.game_stats(datetime.date(year, month, day))
    # takes user to stats page, here we will brainstorm a lot and see what happens
    return render_template('stats_page.html', date={'year': year, 'month': month, 'day': day}, stats=stats)


@app.route('/trivia')
def trivia_page():
    # takes user to about page
    return render_template('trivia_page.html')
