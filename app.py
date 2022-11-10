from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/cakeshopweb-app"
db = SQLAlchemy(app)

class Contact(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    useremail = db.Column(db.String(120), unique=True, nullable=False)
    usersubject = db.Column(db.String(300), nullable=False)
    usermessage = db.Column(db.String(300), nullable=False)

# defining a route
@app.route("/") # decorator
def home():
    return render_template('index.html')

@app.route("/about") 
def about():
    return render_template('about.html')

@app.route("/contact",methods=['GET','POST']) 
def contact():
    if (request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        entry = Contact(username=name,useremail=email,usersubject=subject,usermessage=message)
        db.session.add(entry)
        db.session.commit()


    return render_template('contact.html')

@app.route("/menu") 
def menu():
    return render_template('menu.html')

@app.route("/service") 
def service():
    return render_template('service.html')

@app.route("/team") 
def team():
    return render_template('team.html')

@app.route("/testimonial") 
def testimonial():
    return render_template('testimonial.html')

app.run(debug = True) 