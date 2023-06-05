from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

class PostSerializer(serializers.ModelSerializer):
    user_author = UserSerializer(source='author', read_only=True)
    post_likes = UserSerializer(source='likes', read_only=True, many=True)
    class Meta:
        model = PostModel
        fields = ('__all__')