from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=100, default="")
    city=models.CharField(max_length=100, default="")
    website=models.URLField( default="")
    phone=models.IntegerField(default="")
def create_profile(sender,**kwargs ):
    if kwargs['created']:
        userprofile = user_profile.objects.create(User=kwargs['instance'])
post_save.connect(create_profile,sender=User)


