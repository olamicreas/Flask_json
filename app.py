from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://olamicreas:mujeeb@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
app = Flask(__name__)

@app.route('/')
def welcome():
    person = dict(first='Elie', last='Schoppik', job='Instructor')
    return jsonify(person)