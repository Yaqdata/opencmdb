from flask import Blueprint
from flask_restful import Api

from api.resources.demo import DemoResource
from api.resources.login import LoginResource

api_bp_v1 = Blueprint('bp_v1', __name__)
api_v1 = Api(api_bp_v1, '/v1')

api_v1.add_resource(DemoResource, '/demo')
api_v1.add_resource(LoginResource, '/login')

BLUEPRINTS = [api_bp_v1]

__all__ = ['BLUEPRINTS']
