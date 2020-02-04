from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.utils.safestring import mark_safe
from django import template 

register = template.Library()


@register.filter
def json(obj):
    if isinstance(obj, QuerySet):
        return mark_safe(serialize('json', obj))
    return mark_safe(json.dumps(obj, cls=DjangoJSONEncoder))