import arrow
from flask_mongoengine import QuerySet


class BasicQuerySet(QuerySet):
    def find_by_id(self, _id):
        return self.get(id=_id)

    def find_by_ids(self, _ids):
        return self.filter(id__in=_ids)
