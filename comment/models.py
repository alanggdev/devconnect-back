from django.db import models
from django.contrib.auth.models import User
from post.models import PostModel

class CommentModel(models.Model):
    post_comment = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    description = models.TextField(blank=False)
    date = models.CharField(max_length=25, null=False)