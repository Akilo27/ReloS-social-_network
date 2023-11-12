from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, BlogUser


@login_required
def profile(request, username):
    user_info = UserProfile.objects.get(user__username=username)
    current_user = request.user

    is_current_user = current_user.username == username

    is_admin = current_user.is_superuser

    if is_current_user or is_admin:
        blog = BlogUser.objects.filter(user__username=username).order_by('-date')

        return render(request, 'profile/profile.html', { 'username': username,'user': current_user, 'user_info': user_info, 'blog': blog})

    else:
        # пользователь не имеет доступа к информации о запрашиваемом пользователе
        return HttpResponse("Access Denied")


def handle_like_view(request, username):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        action = request.POST['action']
        user = User.objects.get(username=username)
        BlogUser.handle_like(request, post_id, action, user, username)
    return redirect('profile', username=username)


def edit_profile(request, username):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        years = request.POST['years']
        city = request.POST['city']
        status = request.POST['status']
        about_user = request.POST['about_user']

        user_profile, created = UserProfile.objects.get_or_create(user=User.objects.get(username=username))
        if photo:
            user_profile.image = photo
        if years:
            user_profile.years = years
        if city:
            user_profile.city = city
        if status:
            user_profile.status = status
        if about_user:
            user_profile.about_user = about_user

        user_profile.save()

        return redirect(f'/profile/{username}/')

    return render(request, 'profile/edit_profile.html')


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
    return render(request, 'profile/edit_post.html')


def news_list(request, username):
    user_info = UserProfile.objects.all()
    news = BlogUser.objects.all().order_by('-date')
    return render(request, 'profile/news.html', {'news': news, 'user_info': user_info})


