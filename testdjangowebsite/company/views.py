from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from. serializer import Stockserializers



# list all stocks or     create a new one
#stocks/
class stocklist(APIView):
     def get(self, request):
         stocks= Stock .objects.all()
         serializer= Stockserializers(stocks, many=True)
         return Response(serializer.data)
         pass

     def post(self):
         pass    

# Create your views here.
