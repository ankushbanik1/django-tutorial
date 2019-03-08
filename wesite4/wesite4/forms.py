from django import forms

class EmailForm(forms.Form):
subject = forms.CharField(required=True)
Name= forms.CharField(required=True)
Email = forms.EmailField(required=True)
message = forms.CharField(widget=forms.Textarea, required=True)