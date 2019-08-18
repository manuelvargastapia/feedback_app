from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

# APP INSTANCE
app = Flask(__name__)

# DATABASE
## Switch between environments to set correct database location
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    # Set dev db to "postgresql://[user]:[pass]@[server]/[db]"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/lexus'
else:
    app.debug = False
    # TODO: put prod db here
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

## Initiaize database after configs
db = SQLAlchemy(app)

# MODEL
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200), unique = True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

#  QUERIES
## Create routes using Flask decorator ("/" = home page)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST']) # Handle the POST request from HTML template
def submit():
    if request.method == 'POST':
        # Use request object to get values from inputs (form-group)
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        print("I | [main] submit(): ", customer, dealer, rating, comments)
        # Simple validation
        if customer == "" or dealer == "":
            return render_template('index.html', message='Por favor, ingrese los datos requeridos')
        # Answer to user actions
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0: # Customer doesn't exist
            data = Feedback(customer, dealer, rating, comments) # Create instance based in model
            db.session.add(data) # Add instance to session (no push)
            db.session.commit() # Push data to db
            send_mail(customer, dealer, rating, comments) # Send mail
            return render_template('success.html')
        return render_template('index.html', message='Ya has enviado una evaluación')

# RUN
if __name__ == "__main__":
    app.run() # Run with python app.py in terminal