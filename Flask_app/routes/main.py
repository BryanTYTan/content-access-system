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
    values = {}
    
    all_prods = get_products_available(user_id=session.get('id'))
    
    values['all_prods'] = all_prods
    
    return render_template('product_list.html', values=values)
