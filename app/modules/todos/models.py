# -*- coding: utf-8 -*-

from app.utils.db import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(256), nullable=False, default='')
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
