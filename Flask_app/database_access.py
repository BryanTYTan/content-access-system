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

def _is_access_allowed(product_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT EXISTS (SELECT 1 FROM User_Product WHERE user_id = ? AND product_id = ?)"
    
    cursor.execute(query, ('%' + user_id + '%', '%' + product_id + '%'))
    user_has_access = cursor.fetchone()
    
    return user_has_access
    
    