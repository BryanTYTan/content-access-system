from flask import Blueprint, request, render_template, session, redirect, url_for
from .auth import login_required
from database_access import *

main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    return render_template('index.html', msg='Logged in successfully!')

@main.route('/allProds')
@login_required
def all_products():    
    all_prods, user_owned_products, user_subscribed_products = get_products_available(user_id=session.get('id'))
    
    values = {
        'all_prods': all_prods,
        'owned_prods': user_owned_products,
        'subbed_prods': user_subscribed_products,
    }
    
    return render_template('product_list.html', values=values)
