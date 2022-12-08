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

@app.route("/payment")
def payment():
    return render_template('payment.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')

        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            email=email,
            redirect_url = "http://localhost:5000/success"
        )


        return redirect(response['payment_request']['longurl'])

    else:
        return redirect("/")



app.run(debug=True)
