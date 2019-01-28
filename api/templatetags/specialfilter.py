from django import template

register = template.Library()


@register.filter(name='custom_word')
def custom_word(value):
    word = value[0:2].upper() + value[2:]
    return word
