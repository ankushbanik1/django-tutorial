from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
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