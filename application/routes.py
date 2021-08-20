from application.forms import LoginForm,RegisterForm
from application import app,db
from application.models import User,Course,Enrollment
from flask import render_template,url_for,request,json,Response,redirect,flash

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
    form = RegisterForm()
    return render_template("register.html", form=form,title="New User Registration",register=True)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name},You are successfully logged in!!","success")
            return redirect("/index")
        else:
            flash("Sorry, Something went wrong!!","danger")
    return render_template("login.html",form=form,title="Login")

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
    