from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    title = models.CharField(max_length=10)
    order_by = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username


class BlogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username
