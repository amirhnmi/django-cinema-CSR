from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام کاربری")
    email = models.EmailField(unique=True,verbose_name=" ایمیل")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    phone_number = models.CharField(max_length=14, blank=True, null=True,verbose_name="شماره تماس")
