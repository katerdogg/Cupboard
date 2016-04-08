"""
Seconds to Minutes for total cook time
"""
from django import template

register = template.Library()


@register.filter(name='secondstominutes')
def secondstominutes(seconds):
    return str(int(int(seconds) / 60))
