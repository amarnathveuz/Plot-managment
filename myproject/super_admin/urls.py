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
    

    






]