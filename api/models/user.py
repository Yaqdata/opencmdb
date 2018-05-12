from flask_security import UserMixin
from flask_security.utils import verify_password

from api.models.base import BasicQuerySet
from api.models.role import Role
from extentions import db


class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    meta = {
        'queryset_class': BasicQuerySet
    }

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.objects.filter(email=email).first()

    def verify_password(self, password):
        return verify_password(password, self.password)

