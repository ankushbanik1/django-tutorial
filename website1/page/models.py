from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Paradigm(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
# Create your models here.
class Language(models.Model):
    bangla=models.CharField(max_length=202)
    english=models.CharField(max_length=400)
   

    def __str__(self):
        return self.bangla

class Programmer(models.Model):
    name=models.CharField(max_length=200)        
    def __str__(self):
        return self.name
class Userprofilemanager(models.Manager):
    def get_Queryset(self):
        return super(Userprofilemanager, self).get_Queryset().filter(city='london')




class Userprofile(models.Model):
    user = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    image= models.ImageField(upload_to='profile_img',blank=True)
    london= Userprofilemanager()


    def __str__(self):
        return self.user