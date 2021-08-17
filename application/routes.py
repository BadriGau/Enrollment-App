from application import app
from flask import render_template,url_for
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",index=True)

@app.route("/courses")
def courses():
    courseData = [{"courseID":"1","title":"PHP","description":"Web development with php","credits":"4","term":"Spring"},
                  {"courseID":"2","title":"Python","description":"Web development with Python","credits":"5","term":"Summer"}]
    return render_template("courses.html",courseData=courseData,courses=True)

@app.route("/register")
def register():
    return render_template("register.html",register=True)

@app.route("/login")
def login():
    return render_template("login.html",login=True)
