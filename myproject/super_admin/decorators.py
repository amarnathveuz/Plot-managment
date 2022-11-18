from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from datetime import date

def decorator_fn(args):
    def view_permission_all(func):
        def _wrapped_view(request):
            try:
                uid = user_Details.objects.get(auth_user=request.user.id)
            except:
                pass
            if request.user.is_staff:
                return func(request)
            
            elif uid.user_type == "manager":
                if args == "user_type":
                    status = uid.manager_nav_customer_read_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
                if args == "customer_edit":
                    status = uid.manager_nav_customer_edit_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
                if args == "document_read":
                    status = uid.manager_nav_document_read_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
                if args == "document_write":
                    status = uid.manager_nav_document_write_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
                if args == "document_edit":
                    status = uid.manager_nav_document_edit_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
                if args == "cancel_booking":
                    status = uid.manager_nav_booking_cancel_permission
                    if status == 1:
                        return func(request)
                    else:
                        return HttpResponse("Sorry,You are not allowed to view this page")
            else:
                return HttpResponse("Invalid")
        return _wrapped_view
    return view_permission_all  

