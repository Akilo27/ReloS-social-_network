from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from profiles.models import UserProfile

def main(request):
    return render(request, 'relog/main.html')


# Это представление управляет процессом регистрации
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Проверяет, существует ли уже пользователь с указанным именем пользователя
            if User.objects.filter(username=username).exists():
                return redirect('register')  # Перенаправляет обратно на страницу регистрации, если введено имя пользователя
            else:
                User.objects.create_user(username=username, password=password)  # Создает нового пользователя с
                # указанными именем пользователя и паролем
                UserProfile.objects.create(user=User.objects.get(username=username))
                return redirect('login')  # Перенаправляет на страницу входа в систему после успешной регистрации

    return render(request, 'relog/register.html')


# Это представление обрабатывает процесс входа в систему
def login(request):
    message = 'Добро пожаловать! Введите ваши данные.'
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # Аутентифицирует пользователя с помощью заданного имени пользователя и пароля
        if user is not None:
            auth_login(request, user)


            # Logs in the user if authentication is successful
            return redirect(f'/profile/{username}/', username=username)
            # Перенаправляет на страницу профиля пользователя
        else:
            message = "Нет такого пользователя, просмотрите правильность написания имени и пароля"
            # При сбое аутентификации отображается сообщение об ошибке
    return render(request, 'relog/login.html', {'message': message})


# Это представление обрабатывает процесс выхода из системы
def logout_view(request):
    logout(request)  # Пользователь выходит из системы, очистив свой сеанс
    return redirect('/')
