from django import forms
from.models import status


class statusForm(forms.ModelForm):
    class Meta:
        model= status
        fields={
            'user',
            'content',
            'image'
        }
        #FOR CONTENT LIMIT
    # def clean_content(self,*args,**kwargs):
    #     content =self.content.cleaned_data.get('content')
    #     if len(content)>570:
    #         raise forms.ValidationError('content is too long')
    #     return content    
    def clean(self,*args,**kwargs):
        data = self.cleaned_data
        content=data.get('content',None)
        if content=="":
            content=None
        image=data.get('image',None)
        if content is None and image is None:
            raise forms.ValidationError('content or image is required.')
        return super().clean(*args,**kwargs)  

