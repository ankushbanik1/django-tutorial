from rest_framework import serializers
from. models import Language
from .models import Paradigm
from .models import Programmer
class Languageserializer(serializers.ModelSerializer):
    class Meta:
        

        model= Language
        fields= '__all__'


class Paradigmserializer(serializers.ModelSerializer):
    class Meta:
        model= Paradigm
        fields= '__all__'        


class Programmerserializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        fields= '__all__'        