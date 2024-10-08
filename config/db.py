import logging
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
log = logging.getLogger("example_logger")

def initialize_db(app):

    db_connection_string = os.environ.get("DB_URL")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return db


