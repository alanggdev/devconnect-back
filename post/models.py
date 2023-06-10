from django.db import models
from django.contrib.auth.models import User
# from comment.models import CommentModel

class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='post/media/', null=True)
    date = models.CharField(max_length=25, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # comments = models.ForeignKey(CommentModel, on_delete=models.CASCADE, null=True)