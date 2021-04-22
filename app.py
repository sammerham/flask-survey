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
    session["responses"] = []
    session["question_number"] = 0
    return render_template("survey_start.html", 
    survey_title = title, 
    survey_instructions = instructions)


@app.route("/begin",methods = ["POST"])
def begin_survey():
    """ redirects to questions """
    session["question_number"] = 0
    return redirect(f"/questions/{session['question_number']}")


@app.route("/questions/<int:question_num>")
def display_questions(question_num):
    """ displays current quesstion"""

    question = survey.questions[question_num]
    return render_template('question.html', question = question)

@app.route("/answer", methods=["POST"])
def store_answers():
    """stores answer and redirects to next question"""
    question_answer = request.form["answer"]
    session["responses"].append(question_answer)
    session["question_number"] += 1
    if session["question_number"] >= len(survey.questions):
        return render_template("completion.html")
    else:
        return redirect(f"/questions/{session['question_number']}")
