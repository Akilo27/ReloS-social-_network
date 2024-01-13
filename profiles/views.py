from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, BlogUser
from communitys.models import BlogCommunity

@login_required
def profile(request, username):
    user_info = UserProfile.objects.get(user__username=username)
    current_user = request.user
    is_subscribed = user_info.subscribers.filter(id=current_user.id).exists()

    blog = BlogUser.objects.filter(user__username=username).order_by('-date')
    return render(request, 'profile/profile.html', {'username': username,
                                                    'user': current_user,
                                                    'user_info': user_info,
                                                    'blog': blog,
                                                    'is_subscribed': is_subscribed})


@login_required
def subscribe(request, username):
    if request.method == 'POST':
        user_info = UserProfile.objects.get(user__username=username)
        current_user = request.user
        current_user_info = UserProfile.objects.get(user__username=request.user.username)
        print(user_info, current_user_info, current_user)

        user_info.subscribers.add(current_user)
        current_user_info.subscriptions.add(user_info.user)

        return redirect(request.META['HTTP_REFERER'])


@login_required
def unsubscribe(request, username):
    if request.method == 'POST':
        user_info = UserProfile.objects.get(user__username=username)
        current_user = request.user
        current_user_info = UserProfile.objects.get(user__username=request.user.username)

        user_info.subscribers.remove(current_user)
        current_user_info.subscriptions.remove(user_info.user)

        return redirect(request.META['HTTP_REFERER'])


def handle_like_view(request, username):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        action = request.POST['action']
        user = User.objects.get(username=username)
        BlogUser.handle_like(request, post_id, action, user, username)

    # Получите URL текущей страницы
    referer = request.META.get('HTTP_REFERER')
    if referer:
        # Добавьте якорь к URL страницы
        return redirect(referer + '#post-' + post_id)

    return redirect(request.META.get('HTTP_REFERER'))

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
    news_community = BlogCommunity.objects.all().order_by('-date')

    return render(request, 'profile/news.html', {'news': news,
                                                 'news_community': news_community,
                                                 'user_info': user_info})


def handle_toggle(request, username):
    toggle_status = request.session.get('news_toggle', 'user')

    if toggle_status == 'user':
        request.session['news_toggle'] = 'community'
    elif toggle_status == 'community':
        request.session['news_toggle'] = 'user'

    return redirect('profiles:news', username=username)


@login_required
def friends(request, username):
    all_user_info = UserProfile.objects.all()
    user_info = UserProfile.objects.get(user__username=username)
    friends = user_info.friends.all()
    return render(request, 'profile/friends/friends.html', {'username': username,
                                                            'friends': friends,
                                                            'user_info': user_info,
                                                            'all_user_info': all_user_info})


@login_required
def subscribers(request, username):
    all_user_info = UserProfile.objects.all()
    user_info = UserProfile.objects.get(user__username=username)
    subscribers = user_info.subscribers.all()
    return render(request, 'profile/friends/subscribers.html', {'username': username,
                                                                'subscribers': subscribers,
                                                                'user_info': user_info,
                                                                'all_user_info': all_user_info})


@login_required
def subscriptions(request, username):
    all_user_info = UserProfile.objects.all()
    user_info = UserProfile.objects.get(user__username=username)
    subscriptions = user_info.subscriptions.all()
    return render(request, 'profile/friends/subscriptions.html', {'username': username,
                                                                  'subscriptions': subscriptions,
                                                                  'user_info': user_info,
                                                                  'all_user_info': all_user_info})

@login_required
def add_friend(request, username):
    user_info = UserProfile.objects.get(user__username=username)
    current_user = request.user
    current_user_info = UserProfile.objects.get(user__username=current_user.username)

    user_info.friends.add(current_user)
    current_user_info.friends.add(user_info.user)

    user_info.subscribers.remove(current_user)
    current_user_info.subscriptions.remove(user_info.user)

    return redirect(request.META['HTTP_REFERER'])

def remove_friend(request, username):

    user_info = UserProfile.objects.get(user__username=username)
    current_user = request.user
    current_user_info = UserProfile.objects.get(user__username=current_user.username)

    user_info.friends.remove(current_user)
    current_user_info.friends.remove(user_info.user)

    user_info.subscribers.add(current_user)
    current_user_info.subscriptions.add(user_info.user)

    return redirect(request.META['HTTP_REFERER'])



def delete_blog(request, blog_id):
    blog = BlogUser.objects.get(id=blog_id)
    if blog.user == request.user:
        blog.delete()
    return redirect('profiles:profile', username=request.user.username)
