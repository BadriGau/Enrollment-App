from enum import unique
from flask.wrappers import Response
from application import app,db
from application.models import User,Course,Enrollment
from flask import render_template,url_for,request,json

courseData = [{"courseID":"1","title":"PHP","description":"Web development with php","credits":"4","term":"Spring"},
              {"courseID":"2","title":"Python","description":"Web development with Python","credits":"5","term":"Summer"}]
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",index=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html",courseData=courseData,courses=True,term=term)

@app.route("/register")
def register():
    return render_template("register.html",register=True)

@app.route("/login")
def login():
    return render_template("login.html",login=True)

@app.route("/enrollment",methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html",data={"id":id,"title":title,"term":term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx==None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
        
    return Response(json.dumps(jdata), mimetype="application/json")
  
@app.route("/user")
def user():
    # User(user_id=1, first_name="Badri", last_name="Gautam",email="badrigautam19@gmail.com",password="Bad1234").save()
    # User(user_id=2, first_name="Jean", last_name="Noel",email="jean@gmail.com",password="jean1234").save()
    users = User.objects.all()
    return render_template("user.html",users=users)
    