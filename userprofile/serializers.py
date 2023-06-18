from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfileModel

class UserProfileSerializerModificate(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_profile', read_only=True)
    user_followers = serializers.SerializerMethodField()
    user_following = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileModel
        fields = '__all__'

    def get_user_followers(self, obj):
        follower_profiles = obj.user_followers.all()
        serializer = UserSerializer(follower_profiles, many=True).data
        for user in serializer:
            follower_profile = UserProfileModel.objects.get(user_profile=user['pk'])
            follower_profile_data = UserProfileSerializerModificate(follower_profile).data
            user['profile'] = follower_profile_data['user_avatar']
        return serializer

    def get_user_following(self, obj):
        following_profiles = obj.user_following.all()
        serializer = UserSerializer(following_profiles, many=True).data
        for user in serializer:
            follower_profile = UserProfileModel.objects.get(user_profile=user['pk'])
            follower_profile_data = UserProfileSerializerModificate(follower_profile).data
            user['profile'] = follower_profile_data['user_avatar']
        return serializer

# class UserProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(source='user_profile', read_only=True)
#     user_followers = serializers.SerializerMethodField()
#     user_following = serializers.SerializerMethodField()

#     def get_user_followers(self, obj):
#         followers = obj.user_followers.all()
#         followers_data = UserSerializer(followers, many=True).data
#         for follower_data in followers_data:
#             user_id = follower_data['pk']
#             try:
#                 follower_profile = UserProfileModel.objects.get(user_profile=user_id)
#                 follower_profile_data = UserProfileSerializer(follower_profile).data
#                 follower_data['profile'] = follower_profile_data
#             except UserProfileModel.DoesNotExist:
#                 follower_data['profile'] = None
#         return followers_data

#     def get_user_following(self, obj):
#         following = obj.user_following.all()
#         following_data = UserSerializer(following, many=True).data
#         for follow_data in following_data:
#             user_id = follow_data['pk']
#             try:
#                 following_profile = UserProfileModel.objects.get(user_profile=user_id)
#                 following_profile_data = UserProfileSerializer(following_profile).data
#                 follow_data['profile'] = following_profile_data
#             except UserProfileModel.DoesNotExist:
#                 follow_data['profile'] = None
#         return following_data


#     class Meta:
#         model = UserProfileModel
#         fields = '__all__'
