from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfileModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_profile', read_only=True)
    class Meta:
        model = UserProfileModel
        fields = ('__all__')