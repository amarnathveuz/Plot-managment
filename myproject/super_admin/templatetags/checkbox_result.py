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


@register.filter(name='get_currency_format')
def get_currency_format(value,args):
    print("value::::",str(value))
    print("args:::",str(args))
    ds1 =  '{:20,.2f}'.format(args)
    return ds1