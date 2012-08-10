# -*- coding: UTF-8 -*-

from django import template
from base64 import b64encode

register = template.Library()

@register.filter
def in_group(user, groups):
    """Returns a boolean if the user is in the given group, or comma-separated
    list of groups.

    Usage::

        {% if user|in_group:"Friends" %}
        ...
        {% endif %}

    or::

        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}

    """
    if user.is_authenticated():    
        group_list = groups.split(',')
        return bool(user.groups.filter(name__in=group_list).values('name'))
    else:
        return False
       
       
@register.filter
def dataURI(filename, mime = None):
    """
    This filter will return data URI for given file, for more info go to: 
    http://en.wikipedia.org/wiki/Data_URI_scheme
    
    Sample Usage:
    <img src="{{ "/home/visgean/index.png"|dataURI }}">
    will be filtered into:
    <img src="data:image/png;base64,iVBORw0...">
    """
    
    with open(filename, "rb") as file:
        data = file.read()
    
    encoded = b64encode(data)
    mime = mime + ";" if mime else ";"
    return "data:%sbase64,%s" % (mime, encoded)
    
    
    