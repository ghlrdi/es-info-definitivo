from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.exc import IntegrityError
import requests
from flask import request, redirect, url_for
from decimal import Decimal


app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    products = get_products()
    save_products_to_db(products)
    username = session.get('email')
    return render_template('index.html', products=products, username=username)


def get_products():
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            product_id = product['id']
            existing_product = Product.query.filter_by(product_id=product_id).first()
            if not existing_product:
                new_product = Product(
                    product_id=product_id,
                    name=product['title'],
                    description=product['description'],
                    price=product['price'],
                    image_url=product['image']
                )
                db.session.add(new_product)
        db.session.commit()
        return products
    else:
        return []


def save_products_to_db(products):
    for product_data in products:
        product = Product.query.filter_by(name=product_data['title']).first()
        if not product:
            product = Product(
                name=product_data['title'],
                description=product_data['description'],
                price=product_data['price'],
                image_url=product_data['image'],
                product_id = product_data ['id']
            )
            db.session.add(product)
    db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255))

from sqlalchemy import Sequence

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), db.ForeignKey('users.email'))
    total_amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='active')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)



class CartItem(db.Model):
    __tablename__ = 'cart_items'
    cart_item_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), db.ForeignKey('users.email'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)





def calculate_total(cart_items):
    total = Decimal(0)
    for item in cart_items:
        total += item.price * item.quantity
    return total


@app.route('/checkout', methods=['POST'])
def checkout():
    if 'email' not in session:
        return redirect(url_for('login'))

    user_email = session['email']

    cart_items = CartItem.query.filter_by(user_email=user_email).all()

    total_amount = calculate_total(cart_items)

    max_order_id = Order.query.order_by(Order.order_id.desc()).first()
    if max_order_id:
        new_order_id = max_order_id.order_id + 1
    else:
        new_order_id = 1

    new_order = Order(
        order_id=new_order_id,
        email=user_email,
        total_amount=total_amount
    )
    db.session.add(new_order)
    db.session.commit()

    for cart_item in cart_items:
        order_item = OrderItem(
            order_id=new_order.order_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.price
        )
        db.session.add(order_item)
        db.session.delete(cart_item)

    db.session.commit()

    return redirect(url_for('cart'))




@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    if 'email' not in session:
        return redirect(url_for('login'))

    cart_item_id = request.form.get('cart_item_id')

    cart_item = CartItem.query.get(cart_item_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
    
    return redirect(url_for('cart'))



@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'email' not in session:
        return jsonify({'error': 'Devi effettuare l\'accesso per aggiungere al carrello'}), 401
    
    data = request.json
    product_id = data.get('product_id')
    product = db.session.get(Product, product_id)

    if not product:
        return jsonify({'error': 'Prodotto non trovato nel database'}), 404
    
    user_email = session['email']
    max_cart_item_id = CartItem.query.order_by(CartItem.cart_item_id.desc()).first()
    if max_cart_item_id:
        new_cart_item_id = max_cart_item_id.cart_item_id + 1
    else:
        new_cart_item_id = 1
    
    new_cart_item = CartItem(
        cart_item_id=new_cart_item_id,
        user_email=user_email,
        product_id=product_id,
        quantity=1,
        price=product.price
    )
    db.session.add(new_cart_item)
    db.session.commit()
    
    return jsonify({'success': True}), 200

@app.route('/cart')
def cart():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    user_email = session.get('email')
    cart_items = CartItem.query.filter(CartItem.user_email == user_email).all()
    username = session.get('email')
    return render_template('cart.html', cart_items=cart_items, username=username)





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()

        if not user:
            return jsonify({'error': 'Credenziali non valide'}), 401

        if not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Credenziali non valide'}), 401
        
        session['email'] = user.email
        
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password or not email:
            return jsonify({'error': 'Assicurati di inserire tutti i campi'}), 400
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Email già utilizzata'}), 400
        
        password_hash = generate_password_hash(password)
        
        new_user = User(username=username, password_hash=password_hash, email=email)
        
        db.session.add(new_user)
        db.session.commit()
        
        session['email'] = email
        
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/account')
def account():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    user_email = session['email']
    
    user = User.query.filter_by(email=user_email).first()
    
    if not user:
        return 'Utente non trovato'
    
    return render_template('login.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
