from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import url_for

from src import db
from src import orm

from src.models.user import User
from src.forms.user_form import UserForm

user = Blueprint('user', __name__)

def get_data(form):
    data = dict(
        username = form.username.data,
        email = form.email.data
    )
    return data

@user.route('/user', methods=['GET'])
@orm.db_session
def show_all():
    entries = User.select()
    return render_template('/user/index.html', entries=entries)

@user.route('/user/add', methods=['GET', 'POST'])
@orm.db_session
def add():
    form = UserForm()
    if form.validate_on_submit:
        User(**get_data(form))
        flash('User added')
        return redirect(url_for('user.show_all'))
    return render_template('/user/add.html', form=form)

@user.route('/user/<int:id>', methods=['GET', 'POST'])
@orm.db_session
def edit(id):
    account = User.get(id=id)
    form = UserForm(obj=account)
    if form.validate_on_submit:
        account.set(**get_data(form))
        flash('User updated')
        return redirect(url_for('user.show_all'))
    return render_template('/user/edit.html', form=form, account=account)
    

