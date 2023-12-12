from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Community(models.Model):
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class CommunityProfile(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=100, default='Не указано')
    about_community = models.TextField(default='Не указано')

    subscribers = models.ManyToManyField(User, related_name='subscribers_community', blank=True)

    def __str__(self):
        return self.community.name


class BlogCommunity(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    liked_users = models.ManyToManyField(User, related_name='liked_posts_community', blank=True)

    @staticmethod
    def handle_like(request, post_id, action, community, username):
        post = BlogCommunity.objects.get(id=post_id, community=community)
        if action == 'like':
            post.likes += 1
            post.liked_users.add(request.user)
        elif action == 'unlike':
            post.likes -= 1
            post.liked_users.remove(request.user)
        post.save()

        return redirect('community:detail', name=username)

    def __str__(self):
        return self.community.name
