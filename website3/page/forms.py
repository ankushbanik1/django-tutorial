from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class editprofileForm(UserChangeForm):
    class Meta:
        model=User
        fields={
            'username',
            'email',
            'first_name',
            'password',
        }
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
           