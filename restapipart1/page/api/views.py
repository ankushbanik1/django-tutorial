
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import statusserializer
from page.models import status
from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.views.generic import CreateView,View
from page.forms import statusForm

class statuslistsearchapi(APIView):
    permission_classes     =[]
    authentication_classes =[]


    def get(self,request, format=None):
        qs = status.objects.all()
        serializer= statusserializer(qs,many=True)

        return Response(serializer.data)

    def post(self,request, format=None):
        qs = status.objects.all()
        serializer= statusserializer(qs,many=True)
        return Response(serializer.data)

