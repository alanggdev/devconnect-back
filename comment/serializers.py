from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CommentModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

class CommentSerializer(serializers.ModelSerializer):
    user_author = UserSerializer(source='author', read_only=True)
    class Meta:
        model = CommentModel
        fields = ('__all__')