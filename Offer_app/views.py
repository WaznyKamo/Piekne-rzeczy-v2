from flask import render_template
from Offer_app import app, db
from db_models import Category, Product


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories/', defaults={'category_id': None})
@app.route('/categories/<int:category_id>')
def show_categories(category_id):
    if category_id is None:
        categories = Category.query.all()
        return render_template('categories.html', categories=categories)
    else:
        products_from_category = Product.query.filter_by(category_id=category_id)
        return render_template('products_from_category.html', products=products_from_category)


@app.route('/products')
def show_products():
    products = Product.query.all()
    return render_template('products_from_category.html', products=products)


@app.route('/login')
def login():
    pass
