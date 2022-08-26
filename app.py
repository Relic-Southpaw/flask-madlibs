from flask import Flask, request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def starting():
    adj = story.prompts
    return render_template("base.html", adj = adj)

@app.route('/full')
def filled():
    full = story.generate(request.args)
    return render_template("complete.html", full=full)

