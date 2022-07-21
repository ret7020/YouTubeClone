from flask import Flask, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

from .routings.base import base_bl


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'J06S1rePpx8bmk_h2Xl9CQ' # Random app key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.sqlite' # Database path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Auto reload html/js/css changes without restarting server
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # Upload size limit

    db.init_app(app)

    
    app.register_blueprint(base_bl)


    return app
