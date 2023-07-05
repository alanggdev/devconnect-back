from django.db import models
from django.contrib.auth.models import User

class FileModel(models.Model):
    file = models.FileField(upload_to='files/', null=True)