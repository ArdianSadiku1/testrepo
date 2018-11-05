from flask import flask

app = flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///Users/ardiansadiku/Documents/Python/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False