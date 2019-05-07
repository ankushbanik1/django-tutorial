from django.db import models
from django.conf import settings
from rest_framework import serializers

def upload_status_image(isinstance,filename):
    return "page/{user}/{filename}".format(user=isinstance.user,filename=filename)
class statusqueryset(models.Model):
    pass
class statusmanager(models.Manager):
    def get_queryset(self):
        return statusqueryset(self.model,using=self._db)    
# Create your models here.
class status(models.Model):

    user        =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=True)
    content     = models.TextField()
    image       =models.ImageField(upload_to=upload_status_image,null=True,blank=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)

    objects= statusmanager()

    def __str__(self):
        return str(self.content)[:50]


class Meta:
    verbose_name= "status post"
    verbose_name_plural='status posts'  


