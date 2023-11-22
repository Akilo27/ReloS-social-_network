from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProfileVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ManyToManyField(Video, related_name='video',blank=True)
