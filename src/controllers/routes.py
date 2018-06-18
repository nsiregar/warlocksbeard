''' Routing with Blueprint '''
from src import app

from src.controllers.home import home

app.register_blueprint(home)
