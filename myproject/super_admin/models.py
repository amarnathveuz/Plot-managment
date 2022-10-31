from email.policy import default
from secrets import choice
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.

class intractive_map(models.Model):
    Name = models.CharField(max_length=255, null=True)
    Phoneno = models.CharField(max_length=255, null=True)
    UnitNo = models.IntegerField(null=True)
    UnitNo_primary = models.IntegerField(null=True)
    BlockNo = models.CharField(max_length=255, null=True)
    UnitArea = models.CharField(max_length=255, null=True)
    LandArea = models.CharField(max_length=255, null=True)
    UType = models.CharField(max_length=255, null=True)
    Price = models.FloatField(null=True)
    Bank = models.CharField(max_length=255,null=True)
    Status = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    current_status = models.CharField(max_length=255,null=True)
    attached_file = models.FileField(upload_to="property_image",null=True)

    @property
    def imageURL(self):
        try:
            url = self.attached_file.url
        except:
            url = ''
        return url

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
    ("salesman","salesman")
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


class user_manger_mapping(common):
    user_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_manger_mapping_user_login_id", null=True)
    user_auth_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_manger_mapping_auth_id", null=True)
    manager_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_manger_mapping_manager_id", null=True)



class user_request_plot(common):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_request_plot_login_id", null=True)
    user_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_request_plot_user_login_id", null=True)
    property_mapping_id = models.ForeignKey(intractive_map,on_delete=models.CASCADE,related_name="user_request_plot_user_login_id", null=True)
    name = models.CharField(max_length=255,null=True)
    booking_id = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255,null=True)
    bank = models.CharField(max_length=255,null=True)
    manager_id = models.ForeignKey(user_Details,on_delete=models.CASCADE,related_name="user_request_plot_manager_id", null=True)
    read_status = models.IntegerField(default=0)


