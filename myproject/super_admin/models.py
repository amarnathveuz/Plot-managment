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


class user_Details(common):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="auth_user_login_id", null=True)
    name = models.CharField(max_length=255,null=True)
    

