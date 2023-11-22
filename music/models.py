from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')


class ProfileSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song, related_name='video', blank=True)
