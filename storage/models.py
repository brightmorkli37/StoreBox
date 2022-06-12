from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='my_images/', blank=True, null=True)


class Audio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    audio = models.FileField(upload_to='my_audios/', blank=True, null=True)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='my_videos/', blank=True, null=True)


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='my_documents', blank=True, null=True)