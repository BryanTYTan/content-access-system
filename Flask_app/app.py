from flask import Flask, render_template, request, session, redirect, url_for
import os
from dotenv import load_dotenv

from database_access import *
from routes.main import main
from routes.auth import auth

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    key = os.getenv("SECRET_KEY")
    
    app.secret_key = key
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(debug=True)
