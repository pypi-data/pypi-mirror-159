import datetime
import json
from hashlib import md5
from uuid import UUID

import pytz
from django.db.models.fields.files import ImageFieldFile

from vtb_django_utils.utils.consts import DATETIME_FORMAT


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ImageFieldFile):
            try:
                return obj.path
            except ValueError:
                return ''
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return obj.astimezone(pytz.utc).strftime(DATETIME_FORMAT)
        return json.JSONEncoder.default(self, obj)


def get_json_hash(json_obj):
    return md5(json.dumps(json_obj, sort_keys=True, cls=JSONEncoder).encode()).hexdigest()
