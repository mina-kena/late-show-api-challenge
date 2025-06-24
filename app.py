from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTExtended
from models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTExtended(app)
    
  
    from controllers.auth_controller import auth_bp
    from controllers.episode_controller import episode_bp
    from controllers.guest_controller import guest_bp
    from controllers.appearance_controller import appearance_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)