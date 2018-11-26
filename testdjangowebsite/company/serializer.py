from rest_framework import serializers
from . models import Stock

class Stockserializers(serializers.ModelSerializer):
    class Meta:
        model= Stock
        fields= '__all__'