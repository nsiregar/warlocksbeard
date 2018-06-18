from src import db
from src.helpers.model_helper import BaseModel


class User(BaseModel):
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    def __repr__(self):
        return '<User> {}'.format(self.username)
