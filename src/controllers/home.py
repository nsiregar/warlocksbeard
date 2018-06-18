from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
@home.route('/index', methods=['GET'])
def index():
    return 'TEST'
