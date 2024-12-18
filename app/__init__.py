from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from .api.endpoints import api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app