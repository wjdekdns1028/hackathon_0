from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=10, null = True, blank=True)
    age = models.IntegerField(null = True, blank=True)
    email = models.CharField(max_length=50, null = True, blank=True)
    image = models.ImageField(blank=True)
    genders = {
        ('M', '남성(Man)'), 
        ('W', '여성(Woman)'), 
        ('O', '기타(Other)'),
    }
    gender = models.CharField(verbose_name='성별', max_length=1, choices=genders , null = True, blank=True)
    phone_number = models.CharField(max_length=50, null = True, blank=True)