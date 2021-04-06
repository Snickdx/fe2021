from flask_cors import CORS
from flask import Flask, request, render_template, redirect, flash, url_for, jsonify
from sqlalchemy.exc import IntegrityError
from models import db, Product, Cart #add application models

''' Begin boilerplate code '''

def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  CORS(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

def product_search(search):
    # uncomment after models are implemented
    # return Product.query.filter(
    #     Product.name.like( '%'+search+'%' )
    #     | Product.about.like( '%'+search+'%' )
    #     | Product.category.like( '%'+search+'%' )
    # )
    pass

def cart_total():
    # uncomment after models are implemented
    # items = Cart.query.all()
    # total = 0
    # for item in items:
    #     total += item.product.price * item.quantity
    # return total
    pass

######################### Template Routes ##############################

@app.route('/')
def index():
    return render_template('app.html')


########################### API Routes #############################

@app.route('/app')
def client_app():
    return app.send_static_file('app.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
