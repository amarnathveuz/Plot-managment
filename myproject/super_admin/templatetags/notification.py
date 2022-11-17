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
        property_access = user_data.property_access
        if property_access == 'all':
            data_count = user_request_plot.objects.filter(manager_id_id=user_data.id,read_status=0).count()
        elif property_access == 'plot_based':
            user_access_property_list = user_access_property_mapping.objects.filter(mapping_id_id=user_data.id)
            user_access_property_list_id = list(user_access_property_list.values_list('property_mapping_id',flat=True))
            data_count = user_request_plot.objects.filter(property_mapping_id__in=user_access_property_list_id,manager_id_id=user_data.id,read_status=0).count()
        print("property_access::::::",str(property_access))

        
    return data_count


@register.filter(name='get_loginUsernameImage')
def get_loginUsernameImage(value,args):
    user_dat = User.objects.get(id=value.id)
    st = user_dat.is_superuser
    image_url = ''
    if st == True:
        image_url = 'http://10.10.10.119:8000/static/adminicon.jpg'
    else:
        user_data = user_Details.objects.get(auth_user=value.id)
        if user_data.atatchment == '':
            image_url = 'http://10.10.10.119:8000/static/adminicon.jpg'
        else:    
            image_url ='../media/'+str(user_data.atatchment)

    return image_url


@register.filter(name='get_user_type')
def get_user_type(value,args):
    user_dat = User.objects.get(id=value.id)
    st = user_dat.is_superuser
    if st == True:
        return False
    else:
        user_data = user_Details.objects.get(auth_user=value.id)
        print("user_data.user_type::::::",str(user_data.user_type))
        if user_data.user_type == "manager":
            return True
        else:
            return False

@register.filter(name='get_nav_permission')
def get_nav_permission(value,args):
    user_dat = User.objects.get(id=value.id)
    st = user_dat.is_superuser
    if st == True:
        return True
    else:
        user_data = user_Details.objects.get(auth_user=user_dat)
        if user_data.user_type == "manager":
            if args == "plot_management":
                status = user_data.manager_nav_ploat_permission
                if status == 1:
                    return True
                else:
                    return False
            elif args == "user_management":
                
                status = user_data.manager_nav_user_permission
                if status == 1:
                    return True
                else:
                    return False
            elif args == "property_update_permission":
                
                status = user_data.manager_nav_plot_edit_permission
                if status == 1:
                    return True
                else:
                    return False

        else:
            return False


@register.filter(name='get_user_type_action')
def get_user_type_action(value,args):
    user_dat = User.objects.get(id=value.id)
    st = user_dat.is_superuser
    user_data =""
    try:
        user_data = user_Details.objects.get(auth_user=user_dat)
    except:
        pass
    if st == True:
        return True
    elif user_data.user_type == "manager":
        if args == "user_type":
            status = user_data.manager_nav_customer_read_permission
            if status == 1:
                return True
            else:
                return False
        if args == "customer_edit":
            status = user_data.manager_nav_customer_edit_permission
            if status == 1:
                return True
            else:
                return False
        if args == "document_read":
            status = user_data.manager_nav_document_read_permission
            if status == 1:
                return True
            else:
                return False
        if args == "document_write":
            status = user_data.manager_nav_document_write_permission
            if status == 1:
                return True
            else:
                return False
        if args == "cancel_booking":
            status = user_data.manager_nav_booking_cancel_permission
            if status == 1:
                return True
            else:
                return False
    else:
        return False






    

