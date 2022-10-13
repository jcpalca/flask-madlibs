from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# from stories import silly_story as story
from stories import all_stories_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def story():
    """Show form to pick story"""
    return render_template("select.html",
                          story_list = all_stories_dict.values())

@app.get("/questions")
def questions():
    """Show form with type of word inputs"""
    # selected_story = request.args[story.name]
    story_code = request.args["story_code"]
    story = all_stories_dict[story_code]
    word_types = story.prompts
    return render_template("questions.html", word_types = word_types,
                           story_code = story_code)

@app.get("/<story_code>/results")
# @app.post("/results")
def results(story_code):
    """Show full Madlibs story"""
    story = all_stories_dict[story_code]
    full_story = story.generate(request.args)
    # full_story = story.generate(request.form)
    return render_template("results.html", full_story = full_story)
