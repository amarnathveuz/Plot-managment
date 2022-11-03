from django import template

register = template.Library()

from super_admin.models import *

@register.filter(name='get_notifications')
def get_notifications(value,args):
    user_dat = User.objects.get(id=value.id)
    st = user_dat.is_superuser
    data_count = ''
    if st == True:
        data_count = user_request_plot.objects.filter(read_status=0).count()
    else:
        user_data = user_Details.objects.get(auth_user=value.id)
        data_count = user_request_plot.objects.filter(manager_id_id=user_data.id,read_status=0).count()
    return data_count