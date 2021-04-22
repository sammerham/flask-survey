from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def homepage():
    """return the html that shows survey title, instructions, and start button"""
    title = survey.title
    instructions = survey.instructions

    return render_template("survey_start.html", 
    survey_title = title, 
    survey_instructions = instructions)

@app.route("/begin/questions/<int:question_number>")