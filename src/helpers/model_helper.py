''' Model Helper '''
from src import app
from src import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, _commit=True, **kwargs):
        instance = cls(**kwargs)
        obj = instance.save(_commit)
        return obj

    def update(self, _commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return _commit and self.save or self

    def save(self, _commit=True):
        db.session.add(self)
        if _commit:
            db.session.commit()
        return _commit and db.session.commit()

    def delete(self, _commit=True):
        db.session.delete(self)
        if _commit:
            db.session.commit()
        return _commit and db.session.commit()

