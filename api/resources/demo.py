from api.libs.resource import BaseResource


class DemoResource(BaseResource):
    def get(self):
        return {'test': 'test'}
