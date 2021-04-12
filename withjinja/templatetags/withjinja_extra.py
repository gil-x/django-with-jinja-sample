from django import template

register = template.Library()

@register.filter
def atest(price):   
    return str("Test passed !")

