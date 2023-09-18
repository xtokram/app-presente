from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

class MainRepository():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/app_presente'


    db = SQLAlchemy(app)
