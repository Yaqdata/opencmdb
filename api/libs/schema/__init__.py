from api.libs.schema.user import UserSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)


__all__ = [
    'user_schema', 'users_schema',
]
