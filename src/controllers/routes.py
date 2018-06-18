''' Routing with Blueprint '''
from src import app

from src.controllers.home_controller import home

app.register_blueprint(home)
