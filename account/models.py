from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User , AbstractUser
from .manager import *

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique= True)
    is_verified = models.BooleanField(default = False)
    phone_number = models.CharField(max_length=12)
    otp = models.IntegerField(null=True , blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
