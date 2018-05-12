from functools import wraps
from flask_restful import Resource

from api.libs.error import error
from api.libs.interface_tips import InterfaceTips


class BaseResource(Resource):
    record = None

    @classmethod
    def check_record(cls, model, model_message=None):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if len(list(kwargs.keys())) < 3:
                    record_id = list(kwargs.values())[0]
                    message = model_message if model_message else str(model)
                    record = model.find_by_id(record_id)
                    if record is None:
                        error(InterfaceTips.DATA_NOT_EXISTED, {'model': message})
                    cls.record = record
                return func(*args, **kwargs)
            return wrapper
        return decorate
