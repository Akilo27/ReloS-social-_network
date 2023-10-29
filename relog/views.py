from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth.models import User
from .models import Menu, UserProfile, BlogUser
from PIL import Image

def main(request):
    return render(request, 'relog/main.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('login')

    return render(request, 'relog/register.html')


def login(request):
    menus = Menu.objects.all().order_by('order_by')
    message = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(f'/profile/{username}/', username=username)
        else:
            message="Нет такого пользователя, просмотрите правильность написания имени и пароля"
    return render(request, 'relog/login.html', {'message': message, 'menus': menus})


def profile(request, username):
    try:
        avatar = UserProfile.objects.get(user__username=username)
        avatar = avatar.image.url
    except:
        avatar = None

    blog = BlogUser.objects.filter(user__username=username).order_by('-date')
    print(avatar)
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
