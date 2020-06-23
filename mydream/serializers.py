from rest_framework import serializers
from .models import Destinations1,Destinations2,Cards,About
from django.contrib.auth.models import User


class Destinations2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations2
        fields = ('id', 'description', 'img')

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id', 'description', 'img','heading')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'story', 'img','title')

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')