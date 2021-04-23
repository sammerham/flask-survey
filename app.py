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
    return render_template("survey_start.html", 
    survey = survey)


@app.route("/begin",methods = ["POST"])
def begin_survey():
    """ redirects to questions """
    session["responses"] = []
    return redirect(f"/questions/0")


@app.route("/questions/<int:question_num>")
def display_questions(question_num):
    """ displays current question"""
    responses = session["responses"]
    if len(responses) == len(survey.questions):
        flash("Invalid Question Path")
        return redirect("/complete")
    if len(responses) != question_num:
        flash("Invalid Question Number Input, Please Answer The Next Question:")
        return redirect(f"/questions/{len(responses)}")
    question = survey.questions[question_num]

    return render_template('question.html', question = question)

@app.route("/answer", methods=["POST"])
def store_answers():
    """stores answer and redirects to next question"""
    responses = session["responses"]
    question_answer = request.form["answer"]
    responses.append(question_answer)
    session["responses"] = responses #rebinding session
    if len(responses)>= len(survey.questions):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/complete")
def completion_page():
    """complete page render""" 
    return render_template("completion.html")