from flask import Flask,render_template

app = Flask(__name__)

# defining a route
@app.route("/") # decorator
def home():
    return render_template('index.html')

@app.route("/about") 
def about():
    return render_template('about.html')

@app.route("/contact") 
def contact():
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