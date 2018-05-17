from flask_security import UserMixin
from flask_security.utils import verify_password

from api.models.base import BasicDocument
from api.models.role import Role
from extentions import db


class User(BasicDocument, UserMixin):
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    @classmethod
    def get_user_by_email(cls, email):
        return cls.fetch_one(email=email)

    def verify_password(self, password):
        return verify_password(password, self.password)

