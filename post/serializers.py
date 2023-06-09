from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostModel
from userprofile.models import UserProfileModel

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name')

# class PostSerializer(serializers.ModelSerializer):
#     user_author = UserSerializer(source='author', read_only=True)
#     class Meta:
#         model = PostModel
#         fields = ('__all__')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class PostSerializer(serializers.ModelSerializer):
    user_author = serializers.SerializerMethodField()

    def get_user_author(self, obj):
        user = obj.author
        user_data = UserSerializer(user).data
        user_profile = UserProfileModel.objects.get(user_profile=user)
        user_data['user_profile'] = user_profile.user_avatar.url if user_profile.user_avatar else None
        return user_data

    class Meta:
        model = PostModel
        fields = ('__all__')