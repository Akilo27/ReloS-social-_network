from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import UserProfile, BlogUser


def profile(request, username):
    try:
        avatar = UserProfile.objects.get(user__username=username)
        avatar = avatar.image.url
    except:
        avatar = None
    blog = BlogUser.objects.filter(user__username=username).order_by('-date')
    user = User.objects.get(username=username)
    return render(request, 'relog/profile.html', {'user': user, 'avatar': avatar, 'blog': blog})


def edit_profile(request, username):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        user_profile, created = UserProfile.objects.get_or_create(user=User.objects.get(username=username))
        if photo:
            user_profile.image = photo
            user_profile.save()

        return redirect(f'/profile/{username}/')

    return render(request, 'relog/edit.html')


def edit_post(request, username):
    if request.method == 'POST':
        title = request.POST['title']
        photo = request.FILES.get('photo')
        if title.strip() != '':
            post = BlogUser.objects.create(user=User.objects.get(username=username), title=title)
            if photo:
                post.image = photo
                post.save()
            return redirect(f'/profile/{username}/')
    return render(request, 'relog/edit_post.html')