from django import forms

from home.models import Post
class Homeforms(forms.ModelForm):


    post= forms.CharField(widget=forms.TextInput
    (
        attrs={
            'class':"form-control",
        }
    ))


    class Meta:


         model=Post
         fields=('post', )
x,y=1,2