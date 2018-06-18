from pony import orm
from src import db


class User(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    username = orm.Required(str, unique=True)
    email = orm.Required(str, unique=True)
    first_name = orm.Optional(str)
    last_name = orm.Optional(str)
    password = orm.Required(str)

    def __repr__(self):
        return '<User> {}'.format(self.username)
