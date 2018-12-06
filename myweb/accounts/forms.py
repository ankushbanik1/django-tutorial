from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

from django.contrib.auth.models import User





class registrationform(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        models=User
        field={'username',
        'firstname',
         'lastname',
         'eamil'
        }
def save(self,commit=True):
    user=super(registrationform,self).save(commit=False)
    user.username=cleaned_data['username']
    user.firstname=cleaned_data['firstname']
    user.lastname=cleaned_data['lastname']
    user.password=email_data['email']


    if commit:
        user.save()
    return user



