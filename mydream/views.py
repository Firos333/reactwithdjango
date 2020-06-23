import datetime 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destinations1,Destinations2,Cards,About
from django.contrib import messages
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view
from .serializers import Destinations2Serializer,CardsSerializer,AboutSerializer,CurrentUserSerializer
# Create your views here.
from rest_framework import generics,viewsets


class CarosalListCreate(generics.ListCreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

class AboutListCreate(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer



