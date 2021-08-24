from application.forms import LoginForm,RegisterForm
from application import app,db
from application.models import User,Course,Enrollment
from flask import render_template,url_for,request,json,Response,redirect,flash,session

courseData = [{"courseID":"1","title":"PHP","description":"Web development with php","credits":"4","term":"Spring"},
              {"courseID":"2","title":"Python","description":"Web development with Python","credits":"5","term":"Summer"}]
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",index=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term=None):
    if term is None:
        term="Spring 2019"
    classes = Course.objects.all()
    return render_template("courses.html",courseData=classes,courses=True,term=term)

@app.route("/register",methods=['GET','POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name  = form.last_name.data
        
        user = User(user_id=user_id,email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered !","success")
        return redirect(url_for('index'))
    return render_template("register.html", form=form,title="New User Registration",register=True)

@app.route("/login",methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name},You are successfully logged in!!","success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, Something went wrong!!","danger")
    return render_template("login.html",form=form,title="Login")

@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username',None)
    return redirect(url_for('index'))
    

@app.route("/enrollment",methods=["GET","POST"])
def enrollment():
    if not session.get('username'):
        return redirect(url_for('login'))
    
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get('user_id')
    if courseID:
        if Enrollment.objects(user_id=user_id,courseID=courseID):
            flash(f"You are already enrolled in this course{courseTitle}!","danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id,courseID=courseID).save()
            flash(f"You are enrolled in this course{courseTitle}!","success")
    classes = list( User.objects.aggregate(*[
            {
                '$lookup': {
                    'from': 'enrollment', 
                    'localField': 'user_id', 
                    'foreignField': 'user_id', 
                    'as': 'r1'
                }
            }, {
                '$lookup': {
                    'from': 'course', 
                    'localField': 'r1_courseID', 
                    'foreignField': 'courseID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r1', 
                    'includeArrayIndex': 'r1_id', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'course', 
                    'localField': 'r1.courseID', 
                    'foreignField': 'courseID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'user_id': user_id
                }
            }, {
                '$sort': {
                    'courseID': 1
                }
            }
        ]))
    
    return render_template("enrollment.html",title="Enrollment",classes=classes)




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
    