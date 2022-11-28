from django.db import models

from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from .models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'email',
            'password',
        ]


class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'email',
        ]
    
    def create(self, validated_data):
        #create user
        print(validated_data)
        user = User(
            name = validated_data['name'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user