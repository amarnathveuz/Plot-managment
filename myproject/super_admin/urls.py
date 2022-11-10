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
    # -------amritha update------
    path('next_page_action_url_property',views.next_page_action_url_property,name='next_page_action_url_property'),
    path("property_filter_function",views.property_filter_function, name="property_filter_function"),
    path("property_groupby_action",views.property_groupby_action,name="property_groupby_action"),
    path("property_search_result/", views.property_search_result, name="property_search_result"),

    # ------jiyad update------
    path('user_search_result',views.user_search_result,name="user_search_result"),
    path('next_page_action_url_user', views.next_page_action_url_user, name="next_page_action_url_user"),
    path('grouping_user', views.grouping_user, name="grouping_user"),
    path('filtering_user', views.filtering_user, name="filtering_user"),
    path('logout',auth_views.LogoutView.as_view(),name="logout"),
    path('property_booking_history',views.property_booking_history,name='property_booking_history'),
    path('delete_property_based_access_action',views.delete_property_based_access_action,name='delete_property_based_access_action'),

    path('profile',views.profile,name='profile'),
    path('change_password',views.change_password,name='change_password'),

    path('demo_card_view',views.demo_card_view,name='demo_card_view'),

    path('test_user_detail_page',views.test_user_detail_page,name='test_user_detail_page'),
    


    # ----------new update -----------------
    path('user_type_group_by_action',views.user_type_group_by_action,name='user_type_group_by_action'),
    path('user_search_card_view',views.user_search_card_view,name='user_search_card_view'),
    path('card_view_filter_status',views.card_view_filter_status,name='card_view_filter_status'),
    path('card_view_group_by_status',views.card_view_group_by_status,name='card_view_group_by_status'),
    path('property_groupby_status',views.property_groupby_status,name='property_groupby_status'),
    path('append_card_view',views.append_card_view,name='append_card_view'),
    path('property_search_card_view',views.property_search_card_view,name='property_search_card_view'),

    path('rest_to_available_booking_action_sold_booking',views.rest_to_available_booking_action_sold_booking,name='rest_to_available_booking_action_sold_booking'),
    path('admin_book_plot_action',views.admin_book_plot_action,name='admin_book_plot_action'),
    path('customer_management',views.customer_management,name='customer_management'),
    path('customer_more_details',views.customer_more_details,name='customer_more_details'),
    path('property_card_view_filter_status',views.property_card_view_filter_status,name='property_card_view_filter_status'),
    

    






    
    

    

    

    






]