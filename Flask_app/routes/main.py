from flask import Blueprint, request, render_template, session, redirect, url_for
from .auth import login_required

main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    return render_template('index.html', msg='Logged in successfully!')

@main.route('/allProds')
@login_required
def all_products():
    return render_template('index.html', msg='All products')