from django.db import models
from django.contrib.auth.models import User
from post.models import PostModel

class UserProfileModel(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    # user_avatar = models.ImageField(upload_to='profile/avatar/', null=True)
    # user_description = models.TextField(null=True)
    # user_status = models.CharField(max_length=25, null=True)
    # user_followers = models.ManyToManyField(User, blank=True, related_name='followers')
    # user_following = models.ManyToManyField(User, blank=True, related_name='following')