from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title = "index")

@app.route("/blog")
def blog():
    return render_template('blog.html', title = "blog")


@app.route("/legal")
def legal():
    return render_template('legal.html', title = "legal")