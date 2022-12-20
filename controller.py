from configuration import app
from flask import request, render_template, redirect
from instamojo_wrapper import Instamojo
API_KEY = "test_e7d10a1857a494fd016051d8fcd"
AUTH_TOKEN = "test_d5264a300fc5205c2de74859588"
endpoint = "https://test.instamojo.com/api/1.1/"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint=endpoint)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def service():
    return render_template('services.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    if request.method == 'POST':
        print(name, email, message)
        with open('data.txt', 'a+') as f:
            f.write(str(name) + ' ,' + str(email) + ' ,' + str(message) +'\n')
    return render_template("contact.html")

# @app.route('/save', methods=['GET', 'POST'])
# def save_employee():
#     message = "Invalid email"
#     if request.method == 'POST':
#         formdata = request.form
#
#         email = formdata.get('email')
#         if @ not in email:
#             message = "Invalid email Address..!"
#             return render_template('contact.html', error=message)
#
#         print(formdata)
#         user = User(name=formdata.get('name'),
#                     email=formdata.get('email'),
#                     message=formdata.get('message'),
#         db.session.add(user)
#         db.session.commit()

@app.route("/career")
def career():
    return render_template('career.html')

@app.route("/news")
def news():
    return render_template('new.html')

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


if __name__ == "__main__":
    app.run(debug=True)
