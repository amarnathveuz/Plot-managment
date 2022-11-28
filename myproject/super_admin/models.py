from email.policy import default
from secrets import choice
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.

class Bank_details(models.Model):
    bank_name = models.CharField(max_length=255,null=True)
    bank_identifier_code = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=500,null=True)
    country = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)


class intractive_map(models.Model):
    Name = models.CharField(max_length=255, null=True)
    customer_id_mapping = models.ForeignKey('super_admin.Customer_details',on_delete=models.SET_NULL,related_name="intractive_map_customer_id", null=True)
    customer_id = models.CharField(max_length=255,null=True)
    Phoneno = models.CharField(max_length=255, null=True)
    customer_email = models.CharField(max_length=255,null=True)
    UnitNo = models.IntegerField(null=True)
    UnitNo_primary = models.IntegerField(null=True)
    BlockNo = models.CharField(max_length=255, null=True)
    UnitArea = models.FloatField(max_length=255, null=True)
    LandArea = models.FloatField(max_length=255, null=True)
    UType = models.CharField(max_length=255, null=True)
    Price = models.FloatField(blank=True, null=True)
    Bank = models.CharField(max_length=255,null=True)
    Status = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    current_status = models.CharField(max_length=255,null=True)
    attached_file = models.FileField(upload_to="property_image",null=True)
    currency = models.CharField(max_length=255,null=True,default="SAR")
    Price_currency = models.CharField(max_length=255,null=True)
    bank_relation_id = models.ForeignKey(Bank_details,on_delete=models.CASCADE,related_name="intractive_map_Bank_details_id", null=True)
    

    @property
    def imageURL(self):
        try:
            url = self.attached_file.url
        except:
            url = ''
        return url





class intractive_map_multiple_image(models.Model):
    mapping_id = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="intractive_map_multiple_image_id", null=True)
    attached_file = models.FileField(upload_to="property_multiple_image",null=True)
    image_type = models.CharField(max_length=255,null=True)
    image_name = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255,null=True)
    


class intractive_map_plot_view_image(models.Model):
    mapping_id = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="intractive_map_plot_view_image_map_id", null=True)
    attached_file = models.FileField(upload_to="property_multiple_image_plot_view",null=True)
    image_type = models.CharField(max_length=255,null=True)
    image_name = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    plot_type = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=255,null=True)


from django.utils import timezone
from django.contrib.auth.models import User

class common(models.Model):  # COMM0N
    dt = models.DateField(auto_now=True)
    tm = models.TimeField(auto_now=True)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


password_generate_option = (
    ("Automatic","Automatic"),
    ("Manual","Manual"),
)

login_user_type = (
    ("manager","manager"),
    ("salesman","salesman"),
    ("admin","admin")
)
property_access_option =(
    ("all","all"),
    ("plot_based","plot_based")
)

class user_Details(common):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="auth_user_login_id", null=True)
    name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=255,null=True)
    emp_id = models.CharField(max_length=255,null=True)
    address1 = models.CharField(max_length=255,null=True)
    address2 = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    zip = models.CharField(max_length=255,null=True)
    password_geration_type = models.CharField(max_length=255,choices=password_generate_option,null=True)
    user_type = models.CharField(max_length=255,choices=login_user_type,null=True)
    atatchment = models.FileField(upload_to="user_image",null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="added_by_user_id", null=True)
    plot_list_view = models.CharField(max_length=255,null=True)
    price_visibility = models.IntegerField(null=True,default=1)
    property_access =  models.CharField(max_length=255,choices=property_access_option,null=True)
    manager_nav_ploat_permission = models.IntegerField(default=0)
    manager_nav_user_permission = models.IntegerField(default=0)
    manager_nav_plot_edit_permission = models.IntegerField(default=0)
    manager_nav_booking_cancel_permission = models.IntegerField(default=0)
    manager_nav_customer_read_permission = models.IntegerField(default=0)
    manager_nav_customer_write_permission = models.IntegerField(default=0)
    manager_nav_customer_edit_permission = models.IntegerField(default=0)
    manager_nav_document_read_permission = models.IntegerField(default=0)
    manager_nav_document_write_permission = models.IntegerField(default=0)
    manager_nav_document_edit_permission = models.IntegerField(default=0)

class user_access_property_mapping(common):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_access_property_mapping_auth_id", null=True)
    mapping_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_access_property_mapping_id", null=True)
    property_mapping_id  = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="user_access_property_mapping_property_id", null=True)


class user_manger_mapping(common):
    user_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_manger_mapping_user_login_id", null=True)
    user_auth_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_manger_mapping_auth_id", null=True)
    manager_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_manger_mapping_manager_id", null=True)

customer_comapny_type =(
    ("individual","individual"),
    ("company","company")
)

class Customer_details(common):
    name =  models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255,null=True)
    customer_email = models.CharField(max_length=255,null=True)
    customer_id = models.CharField(max_length=255,null=True)
    bank =  models.CharField(max_length=255,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Customer_details_created_by", null=True)
    customer_type = models.CharField(max_length=255,choices=customer_comapny_type,null=True)
    company_name =  models.CharField(max_length=255,null=True)
    street1 =  models.CharField(max_length=255,null=True)
    street2 =  models.CharField(max_length=255,null=True)
    city =  models.CharField(max_length=255,null=True)
    satte =  models.CharField(max_length=255,null=True)
    zip =  models.CharField(max_length=255,null=True)
    email =  models.CharField(max_length=255,null=True)
    customer_doc_id = models.FileField(upload_to="customer_document",null=True)
    contract_certi = models.FileField(upload_to="customer_document",null=True)
    tax_certificate  = models.FileField(upload_to="customer_document",null=True)
    other_document = models.FileField(upload_to="customer_document",null=True)
    bank_relation_id = models.ForeignKey(Bank_details,on_delete=models.CASCADE,related_name="Customer_details_Bank_details_id", null=True)
    profile_pic = models.FileField(upload_to="customer_document",null=True)
    customer_doc_id_update_dt = models.DateField(null=True)
    contract_certi_update_dt = models.DateField(null=True)
    tax_certificate_update_dt = models.DateField(null=True)
    other_document_update_dt = models.DateField(null=True)
    customer_doc_id_extesion = models.CharField(max_length=255,null=True)
    contract_certi_extesion = models.CharField(max_length=255,null=True)
    tax_certificate_extesion = models.CharField(max_length=255,null=True)
    other_document_extesion = models.CharField(max_length=255,null=True)
    customer_doc_id_name = models.CharField(max_length=255,null=True)
    contract_certi_name = models.CharField(max_length=255,null=True)
    tax_certificate_name = models.CharField(max_length=255,null=True)
    other_document_name = models.CharField(max_length=255,null=True)




    

class user_request_plot(common):
    customer_id = models.ForeignKey(Customer_details,on_delete=models.CASCADE,related_name="user_request_plot_customer_id", null=True)
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_request_plot_login_id", null=True)
    user_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_request_plot_user_login_id", null=True)
    property_mapping_id = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="user_request_plot_user_login_id", null=True)
    name = models.CharField(max_length=255,null=True)
    booking_id = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255,null=True)
    customer_email = models.CharField(max_length=255,null=True)
    bank = models.CharField(max_length=255,null=True)
    manager_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_request_plot_manager_id", null=True)
    read_status = models.IntegerField(default=0)
    booking_status = models.IntegerField(null=True)
    reset_to_availale = models.IntegerField(null=True)
    available_status = models.IntegerField(default=1)
    bank_relation_id = models.ForeignKey(Bank_details,on_delete=models.CASCADE,related_name="user_request_plot_Bank_details_id", null=True)
    customer_doc_id = models.FileField(upload_to="customer_document",null=True)
    contract_certi = models.FileField(upload_to="customer_document",null=True)
    tax_certificate  = models.FileField(upload_to="customer_document",null=True)
    other_document = models.FileField(upload_to="customer_document",null=True)
    Price = models.FloatField(blank=True, null=True)



login_user_type = (
    ("administrator","administrator"),
    ("staff","staff")
)

class booking_log(common):
    booking_id = models.ForeignKey(user_request_plot,on_delete=models.CASCADE,related_name="booking_log_id", null=True)
    intractive_map_id = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="booking_log_intractive_map_id_id", null=True)
    action_appy_user = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="booking_log_user_login_id", null=True)
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="booking_log_auth_login_id", null=True)
    user_type = models.CharField(max_length=255,choices=login_user_type,null=True)
    d_text = models.TextField(null=True)
    status_content = models.TextField(null=True)
    log_type = models.CharField(max_length=255,choices=login_user_type,null=True)
    assigned_user_id =  models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="booking_log_assign_user_login_id", null=True)



class user_log(common):
    user_mapping_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_log_login_id", null=True)
    action_appy_user = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_log_user_login_id", null=True)
    action_auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_log_auth_login_id", null=True)
    d_text = models.TextField(null=True)
    status_content = models.TextField(null=True)
    user_type = models.CharField(max_length=255,choices=login_user_type,null=True)





class status_code(common):
    text = models.CharField(max_length=255,null=True)
    status_code = models.IntegerField(null=True)



class plot_view_master(common):
    unit_type = models.CharField(max_length=255,null=True)

class plot_view_master_image(common):
    mapping_id = models.ForeignKey(plot_view_master,on_delete=models.CASCADE,related_name="plot_view_master_mapping_id", null=True)
    attached_file = models.FileField(upload_to="plot_view_master_image",null=True)
    image_type = models.CharField(max_length=255,null=True)
    image_name = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    plot_type = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=255,null=True)



class new_user(common):
    fname = models.CharField(max_length=255,null=True)