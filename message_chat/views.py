from django.contrib.auth.models import User
from django.shortcuts import render

from .models import MessageChat


def messages(request, username):
    user = User.objects.get(username=username)
    message = MessageChat.objects.filter(Q(first_user=user) | Q(second_user=user))
    distinct_message = MessageChat.objects.filter(Q(first_user=user) | Q(second_user=user)).values('id', 'first_user', 'second_user').distinct()
    message = message.union(distinct_message)
    print(message)

    return render(request, 'message/message_chat.html', {'message_chat': message})
