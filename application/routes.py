from application import app
from flask import render_template,url_for
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",login=False)

@app.route("/courses")
def courses():
    return "<p>courses</p>"

@app.route("/register")
def register():
    return "<p>courses</p>"

@app.route("/login")
def login():
    return "<p>courses</p>"
