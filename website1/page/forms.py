from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class editprofileform(UserChangeForm):
    class Meta:
        model=User
        fields={
           
            'email',
            'first_name',
            'last_name',
            'password',
        }
        
