from django.contrib.auth.models import User
from django.db import models



class MessageChat(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user')
    message_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
