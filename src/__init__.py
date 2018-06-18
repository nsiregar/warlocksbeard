from flask import Flask
from pony import orm
from config.application import DevelopmentConfig

app = Flask(__name__, static_folder='assets', template_folder='views')
app.config.from_object('config.application.DevelopmentConfig')
db = orm.Database()
db.bind(DevelopmentConfig.DATABASE_PROVIDER, **DevelopmentConfig.DATABASE_CONFIG)
db.generate_mapping(create_tables=True)

from src.controllers import routes
