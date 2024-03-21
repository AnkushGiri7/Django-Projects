from django import template
from datetime import datetime


register = template.Library()

# @register_filter.filter(name = "printDate",is_safe=True)
# def printDate():
#     return datetime.now().strftime("%d-%m-%y")

# register_filter.filter("printDate",printDate)

@register.filter(name="multiply")
def multiply(v1,v2):
    return v1*v2