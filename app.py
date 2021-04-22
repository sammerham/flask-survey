from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """return the html that shows survey title, instructions, and start button"""
    title = survey.title
    instructions = survey.instructions
    session['responses'] = []
    return render_template("survey_start.html", 
    survey_title = title, 
    survey_instructions = instructions)


@app.route("/begin",methods = ["POST"])
def begin_survey():
    """ Starts the survery"""
    return redirect('/questions/0')


@app.route('/questions/<int:question_num>')
def display_questions(question_num):
    question = survey.questions[question_num]
    return render_template('question.html', question =question)
