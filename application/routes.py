from application import app
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Welcome to Enrollment site</h1>"