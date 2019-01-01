from django.db import models


class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eddr=models.CharField(max_length=200)
# Create your models here.
