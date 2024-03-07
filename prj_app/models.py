from django.db import models

# Create your models here.
class alluser(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128) 

class register(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128) 
    user_type = models.CharField(max_length=50, default='public')
    last_login = models.DateTimeField(verbose_name='last_login',blank=True,null=True)