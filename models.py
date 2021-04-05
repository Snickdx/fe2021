from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    price =  db.Column(db.Float, nullable=False)
    image = db.Column(db.String(400), nullable=False)
    about = db.Column(db.String(200), nullable=False)
    carts = db.relationship('Cart', backref='product', lazy=True)
    
    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'image': self.image,
            'about' : self.about
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), unique=True, nullable=False)


    def toDict(self):
        return{
            'id': self.id,
            'quantity': self.quantity,
            'product_id': self.product_id,
            'name': self.product.name,
            'price': self.product.price
        }
