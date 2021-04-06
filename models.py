from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)