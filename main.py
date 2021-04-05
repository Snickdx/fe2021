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

def product_filter(search):
    return Product.query.filter(
        Product.name.like( '%'+search+'%' )
        | Product.about.like( '%'+search+'%' )
        | Product.category.like( '%'+search+'%' )
    )

def cart_total():
    items = Cart.query.all()
    total = 0
    for item in items:
        total += item.product.price * item.quantity
    return total

######################### View Routes ##############################

@app.route('/')
def index():
    search = request.args.get('search')
    products = None
    if search:
        products = product_filter(search)
    else:
        products = Product.query.all()
    cart = Cart.query.all()
    total = cart_total
    return render_template('app.html', products=products, cart=cart, total=total)

@app.route('/cart/<id>', methods=['GET'])
def add_action(id):
    cart = Cart(
        quantity=1, 
        product_id=id,
    )
    db.session.add(cart)
    db.session.commit()
    return redirect('/')

@app.route('/api/cart/<id>', methods=['POST'])
def edit_action(id):
    data = request.form
    cart = Cart.query.get(id)
    if data['quantitiy'] == 0:
        db.session.delete(cart)
    else:
        db.session.add(cart)
    db.session.commit()
    return redirect('/')


########################### API Routes #############################

@app.route('/app')
def client_app():
  return app.send_static_file('app.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    search = request.args.get('search')
    products = None
    if search:
        products = product_filter(search)
    else:
        products = Product.query.all()
    products = [product.toDict() for product in products]
    return jsonify(products)

@app.route('/api/cart', methods=['GET'])
def get_cart():
    cart = Cart.query.all()
    cart = [item.toDict() for item in cart]
    total = cart_total()

    return jsonify({ "total":total,  "cart":cart} )

@app.route('/api/cart', methods=['POST'])
def add_cart():
    data = request.json
    cart = Cart(
        quantity=data['quantity'], 
        product_id=data['product_id'],
    )
    db.session.add(cart)
    db.session.commit()
    return jsonify({'message': 'Created'})

@app.route('/api/cart/<id>', methods=['PUT'])
def edit_cart(id):
    data = request.json
    cart = Cart.query.get(id)
    cart.quantity = data['quantity']
    if data['quantity'] == 0:
        db.session.delete(cart)
    else:
        db.session.add(cart)
    db.session.commit()
    return jsonify({'message': 'Updated'})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
