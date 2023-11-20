from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import MessageChat
from profiles.models import UserProfile


def chat(request, username):
    chats = MessageChat.objects.exclude(first_user=request.user) | MessageChat.objects.exclude(second_user=request.user)
    user_info = UserProfile.objects.all()
    user_names = []
    for chat in chats:
        user_names.append(chat.first_user.username)
        user_names.append(chat.second_user.username)
    user_names = list(set(user_names))

    return render(request, 'message/chats.html', {'user_names': user_names, 'user_info': user_info})


@login_required
def dialog(request, username):
    chat_user = get_object_or_404(User, username=username)
    user_info = UserProfile.objects.all()
    chats = MessageChat.objects.filter(first_user=request.user, second_user=chat_user) | MessageChat.objects.filter(
        second_user=request.user, first_user=chat_user)

    if request.method == 'POST':
        first_user = request.user
        second_user = chat_user
        message_text = request.POST['message_text']
        image = request.FILES.get('image')
        chat = MessageChat.objects.create(first_user=first_user, second_user=second_user, message_text=message_text)
        if image:
            chat.image = image
            chat.save()
        chat.save()
        return redirect('messages', username=username)

    return render(request, 'message/messages.html', {'chats': chats, 'chat_user': chat_user, 'user_info': user_info})
