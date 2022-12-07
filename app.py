from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def service():
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/career")
def career():
    return render_template('career.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

app.run(debug=True)



