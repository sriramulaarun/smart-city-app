from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    from app.routes.api import bp as api_bp
    app.register_blueprint(api_bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/smartcity.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('SmartCity startup')

    return app
