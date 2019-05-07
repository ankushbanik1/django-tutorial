from rest_framework import serializers
from page.models import status

class statusserializer(serializers.ModelSerializer):
    class Meta:
        model= status
        field={
            'user',
            'content',
            'image'
        }
    # def validate_content(self,value)    :
    #     if len(value)>10000:
    #         raise serializers.ValidationError('this is too long!')
    #     return value

    def validate(self,data):
        content=data.get('content',None)
        if content=="":
            content=None
        image=data.get('image',None)
        if content is None and image is None:
            raise serializers.ValidationError('content or image is required.')  
        return data      