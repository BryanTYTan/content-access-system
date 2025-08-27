import sqlite3
from flask import render_template, request, session, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_products_available():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get available products in db
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()
    
    return render_template('product_list.html', products=products)