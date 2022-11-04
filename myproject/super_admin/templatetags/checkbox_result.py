from django import template
register = template.Library()
from super_admin.models import *



@register.filter(name='check_action')

def check_action(value,args):
    print("value:::::",str(value))
    print("args::",str(args))
    
    if str(value) in args:
        return True
    else:
        return False