from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    exprience=(
        ('Less then 1 yr','Less then 1 yr'),
        ('Less then 2 yr','Less then 2 yr'),
        ('Less then 3 yr','Less then 3 yr'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    description=models.CharField(max_length=100, default="")
    city=models.CharField(max_length=100, default="")
    website=models.URLField( default="")
    phone=models.IntegerField(default="")
@receiver(post_save,sender=User)
def create_user_profile(sender,instance, created,**kwargs):
    if created:
       Profile.objects.created(User=instance)
@receiver(post_save,sender=User)
def save_user_profile(ender,instance,**kwarg):
    instance.profile.save()
















