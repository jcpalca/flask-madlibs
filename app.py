from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/questions")
def questions():
    word_types = story.prompts
    return render_template("questions.html", word_types = word_types)

@app.get("/results")
def results():
    full_story = story.generate(request.args)
    return render_template("results.html", full_story = full_story)

