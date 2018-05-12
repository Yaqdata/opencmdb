from flask_security import UserMixin

from api.models.base import BasicQuerySet
from extentions import db


class Role(db.Document, UserMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    meta = {
        'queryset_class': BasicQuerySet
    }

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
