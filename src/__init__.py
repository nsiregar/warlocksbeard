from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='assets', template_folder='views')
app.config.from_object('config.application.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.controllers import routes
