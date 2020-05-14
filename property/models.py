from django.db import models
from datetime import datetime
# Create your models here.

class MemberDetail(models.Model):
    user_name = models.CharField(max_length=30,null=False,unique=True)
    first_name = models.CharField(max_length=20,null=False,default=None)
    last_name = models.CharField(max_length=20,null=False,default=None)
    email = models.EmailField(max_length = 50, blank=False,default=None,unique=True)
    contact = models.CharField(max_length=150,default=None)
    password = models.CharField(max_length=150,blank=False,default=None)
    created_at = models.DateTimeField(default=datetime.now(), blank=False)
    ip_address  =models.GenericIPAddressField(blank=False)
    is_active = models.BooleanField('is_active', default=False)
    last_login = models.DateTimeField(default=datetime.now(), blank=False)