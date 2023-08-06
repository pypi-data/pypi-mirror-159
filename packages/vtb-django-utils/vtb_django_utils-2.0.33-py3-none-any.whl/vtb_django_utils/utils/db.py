from functools import lru_cache
from typing import List, Optional, Union, Type

from django.db import models

from vtb_django_utils.utils.consts import DATETIME_SHORT_FORMAT


class CreatedMixin(models.Model):
    create_dt = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('create_dt',)

    @property
    def create_str(self):
        return self.create_dt.strftime(DATETIME_SHORT_FORMAT)


class CreateUpdatedMixin(CreatedMixin, models.Model):
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('create_dt',)

    @property
    def update_str(self):
        return self.update_dt.strftime(DATETIME_SHORT_FORMAT)


@lru_cache
def get_model_fields(model_class: Type[models.Model], exclude: Union[tuple, list] = None) -> List[models.Field]:
    """ Возвращает список полей модели БД """
    exclude_set = set(exclude or [])
    return [f for f in model_class._meta.fields if f.name not in exclude_set]


@lru_cache
def get_model_field_names(model_class: Type[models.Model], exclude: Union[tuple, list] = None) -> List[str]:
    """ Возвращает список полей модели БД """
    exclude_set = set(exclude or [])
    return [f.attname for f in model_class._meta.fields if f.name not in exclude_set]


@lru_cache
def get_rel_model_fields(model_class: Type[models.Model], exclude: Union[tuple, list] = None) -> List[str]:
    """ Возвращает список реляционных полей модели БД """
    exclude_set = set(exclude or [])
    return [f.name for f in model_class._meta.fields
            if f.name not in exclude_set and getattr(f, 'foreign_related_fields', None)]


def create_model_from_dict(model_class: Type[models.Model], data: dict,
                           ignore_fields: Optional[Union[list, tuple]] = None):
    """ Создает экземпляр модели в БД из словаря """
    db_field_names = set(get_model_field_names(model_class))
    ignore_fields = ignore_fields or []
    return model_class.objects.create(**{
        k: v for k, v in data.items()
        if k in db_field_names and k not in ignore_fields}
    )


@lru_cache
def not_required_model_fields(model_class: Type[models.Model]) -> list:
    """ Возвращает необязательные поля модели """
    return [field.attname for field in model_class._meta.fields if field.null]
