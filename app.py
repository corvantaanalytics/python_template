from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config.routes import initialize_routes
from config.db import initialize_db
from config.logging import get_logger

def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)

    # Load environment variables from .env file
    load_dotenv()

    # Set up logging
    logger = get_logger()

    # Initialize the database
    initialize_db(app)

    # Initialize routes
    initialize_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    # Run the app
    app.run(debug=True, use_reloader=False, port=5000, threaded=True)
