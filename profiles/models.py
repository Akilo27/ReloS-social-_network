from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    years = models.IntegerField(default=18)
    city = models.CharField(max_length=100, default='Не указано')
    status = models.CharField(max_length=100, default='Не указано')
    about_user = models.TextField(default='Не указано')

    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)
    subscriptions = models.ManyToManyField(User, related_name='subscriptions', blank=True)

    def __str__(self):
        return self.user.username


class BlogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    liked_users = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    @staticmethod
    def handle_like(request, post_id, action, user, username):
        post = BlogUser.objects.get(id=post_id)
        if action == 'like':
            post.likes += 1
            post.liked_users.add(user)
        elif action == 'unlike':
            post.likes -= 1
            post.liked_users.remove(user)
        post.save()

        return redirect('profile',username=username)

    def __str__(self):
        return self.user.username
