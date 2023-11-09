from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth.models import User
from .models import Menu
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
            message = "Нет такого пользователя, просмотрите правильность написания имени и пароля"
    return render(request, 'relog/login.html', {'message': message, 'menus': menus})
