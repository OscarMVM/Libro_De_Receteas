from rest_framework import serializers
from .models import Client
from rest_framework.response import Response
from rest_framework.serializers import (
    ModelSerializer
)

class postSerializer(ModelSerializer):
    class Meta:
        model=Client
        fields=['id', 'email', 'password']