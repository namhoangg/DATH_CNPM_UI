#from flask import Blueprint, render_template, request

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import or_
from .model import Buyer, Product
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home(): 
    top_discounted_products = Product.query.order_by(Product.discount.desc()).limit(5).all()
    return render_template('homepage.html', products=top_discounted_products)

@views.route('/list-view')
def list_view():
    products = Product.query.all()  # Fetches all products
    return render_template('list-view.html', products=products)

@views.route('/search-results')
def search_results():
    keyword = request.args.get('keyword', '')
    category = request.args.get('category', 'all')

    query = Product.query

    if keyword:
        query = query.filter(Product.name.ilike(f'%{keyword}%'))  # Adjust the Product.name to your model

    if category != 'all':
        query = query.filter_by(category=category)  # Adjust the Product.category to your model

    products = query.all()
    return render_template('list-view.html', products=products)

@views.route('/apply-filters')
def apply_filters():
    selected_brands = request.args.getlist('brand')
    min_price = request.args.get('min_price', type=float, default=0.0)
    max_price = request.args.get('max_price', type=float, default=float('inf'))
    selected_ratings = request.args.getlist('rating', type=int)

    query = Product.query

    if selected_brands:
        query = query.filter(Product.brand.in_(selected_brands))
    
    query = query.filter(Product.price >= min_price, Product.price <= max_price)
  
    if selected_ratings:
        rating_filters = []
        for rating in selected_ratings:
            if rating == 5:
                rating_filters.append(Product.review_rating >= 5)
            else:
                rating_filters.append((Product.review_rating >= rating) & (Product.review_rating < rating + 1))
        
        if rating_filters:
            query = query.filter(or_(*rating_filters))

    products = query.all()
    return render_template('list-view.html', products=products)