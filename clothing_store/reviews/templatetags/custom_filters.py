from django import template

register = template.Library()

@register.filter
def to_int(number):
    try:
        return int(number)
    except ValueError:
        return 0