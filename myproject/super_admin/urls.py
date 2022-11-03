from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('plot',views.plot,name='plot'),
    path('home',views.home,name='home'),
    path('property_management',views.property_management,name='property_management'),
    path('create_property',views.create_property,name='create_property'),
    path('user_management',views.user_management,name='user_management'),
    path('create_user',views.create_user,name='create_user'),
    path('upload_excel',views.upload_excel,name='upload_excel'),
    path('simple_upload',views.simple_upload,name='simple_upload'),
    path('property_list_api',views.property_list_api,name='property_list_api'),
    path('property_list_api/<int:pk>',views.property_list_api1,name='property_list_api1'),
    path('property_update',views.property_update,name='property_update'),
    path('user_edit',views.user_edit,name='user_edit'),
    path('update_user_action',views.update_user_action,name='update_user_action'),
    path('login_action',views.login_action,name='login_action'),
    path('booking_action',views.booking_action,name='booking_action'),
    path('view_all_activity',views.view_all_activity,name='view_all_activity'),
    path('booking_more_details',views.booking_more_details,name='booking_more_details'),
    path('approve_booking_action',views.approve_booking_action,name='approve_booking_action'),
    path('cancel_booking_action',views.cancel_booking_action,name='cancel_booking_action'),
    path('rest_to_available_booking_action',views.rest_to_available_booking_action,name='rest_to_available_booking_action'),
    path('delete_image_action',views.delete_image_action,name='delete_image_action'),
    path("export_excel/", views.export_data_to_excel, name="export_excel"),
    path('plot_table_view',views.plot_table_view,name='plot_table_view'),
    path('user_based_property_delete',views.user_based_property_delete,name='user_based_property_delete'),
    
    

    

    

    






]