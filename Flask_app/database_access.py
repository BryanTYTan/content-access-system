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
    
    cursor.close()
    return products

def _is_access_allowed(product_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT EXISTS (SELECT 1 FROM User_Product WHERE user_id = ? AND product_id = ?)"
    
    cursor.execute(query, ('%' + user_id + '%', '%' + product_id + '%'))
    user_has_access = cursor.fetchone()
    
    cursor.close()
    return user_has_access
    
def _publish_pack(pack_id, user_id):
    reply = {
        'status': False,
        'msg': ""
    }
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    pack_query = "SELECT id,product_id,published FROM Pack WHERE id = ?"
    
    cursor.execute(pack_query, ('%' + pack_id + '%'))
    Pack = cursor.fetchone()
    
    if Pack:
        # Get parent product
        product_query = "SELECT id FROM Product WHERE id = ?"
        
        cursor.execute(product_query, ('%' + Pack.product_id + '%'))
        Product = cursor.fetchone()
        
        # Verify if user owns product
        user_owns = _is_access_allowed(Product.id, user_id)
        
        if user_owns:            
            pub_val = not Pack.published
            
            update_query = "UPDATE Pack SET published = ? WHERE id = ?"
            cursor.execute(update_query, ('%' + pub_val + '%', '%' + Pack.id + '%'))
            
            reply['status'] = True
            reply['msg'] = "Product Updated"
            
        else:
            reply['msg'] = "User does not own product"

    else:
        reply['msg'] = "Pack does not exist"

    cursor.close()
    return reply