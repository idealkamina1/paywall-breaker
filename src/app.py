from flask import Flask
from src.api.routes import api_routes

def create_app():
    app = Flask(__name__)
    
    # Register API routes
    app.register_blueprint(api_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)