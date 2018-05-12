from flask import Flask
from flask_security import MongoEngineUserDatastore

from api.config import load_config
from api.libs.error import error
from api.libs.interface_tips import InterfaceTips
from api.models import User, Role
from api.resources import BLUEPRINTS
from extentions import (db, security)


def create_app(app_name='api', blueprints=None):
    app = Flask(app_name)
    config = load_config()
    app.config.from_object(config)

    if not blueprints:
        blueprints = BLUEPRINTS

    blueprints_resister(app, blueprints)
    extensions_load(app)
    return app


def extensions_load(app):
    db.init_app(app)
    user_data_store = MongoEngineUserDatastore(db, User, Role)
    s = security.init_app(app, user_data_store, register_blueprint=False)

    # TODO 无法分辨token过期/没有token/无效的token
    def unauthorized_handler():
        error(InterfaceTips.INVALID_TOKEN)
    s.unauthorized_handler(unauthorized_handler)


def blueprints_resister(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)
