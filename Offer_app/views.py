from flask import render_template
from Offer_app import app, db
from sqlalchemy.sql import select


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories/', defaults={'client_id': None})
@app.route('/api/categories/<int:category_id')
def show_categories(category_id):
    if category_id is None:
        pass
    else:

        products_from_category = select([db.products])
