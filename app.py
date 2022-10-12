from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/questions")
def questions():
    """Show form with type of word inputs"""
    word_types = story.prompts
    return render_template("questions.html", word_types = word_types)

@app.get("/results")
# @app.post("/results")
def results():
    """Show full Madlibs story"""
    full_story = story.generate(request.args)
    # full_story = story.generate(request.form)
    return render_template("results.html", full_story = full_story)
