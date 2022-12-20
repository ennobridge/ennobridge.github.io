from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instamojo_wrapper import Instamojo
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/myproject'
db = SQLAlchemy(app)