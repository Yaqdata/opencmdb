import arrow
from flask_mongoengine import QuerySet, Document
from extentions import db


class BasicDocument(Document):
    updated_at = db.DateTimeField(default=lambda: arrow.now().datetime)
    created_at = db.DateTimeField(default=lambda: arrow.now().datetime)

    meta = {
        'abstract': True,
        'queryset_class': QuerySet,
        'indexes': [
            '-updated_at',
            '-created_at'
        ]
    }

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.pk)

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.pk)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        return obj.save()

    def update(self, **kwargs):
        kwargs['updated_at'] = arrow.now().datetime
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self.save()

    @classmethod
    def fetch_all(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    @classmethod
    def fetch_one(cls, **kwargs):
        return cls.objects.filter(**kwargs).first()

    @classmethod
    def find_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def find_by_pks(cls, pks):
        return cls.objects.filter(pk__in=pks)
