from django import template
from django.template.defaultfilters import stringfilter
from django.utils.timesince import timesince
from datetime import datetime, timedelta
from django.utils.timezone import is_aware, utc

register = template.Library()

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.filter
def age(value):
    now = datetime.now(utc if is_aware(value) else None)
    try:
        difference = now - value
    except:
        return value

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s yang lalu' % {'time': timesince(value).split(', ')[0]}