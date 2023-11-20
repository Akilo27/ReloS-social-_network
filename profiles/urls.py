
from django.urls import path
from . import views


app_name = 'profiles'


urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),

    path('<str:username>/friends/', views.friends, name='friends'),
    path('<str:username>/subscribers/', views.subscribers, name='subscribers'),
    path('<str:username>/subscriptions/', views.subscriptions, name='subscriptions'),

    path('<str:username>/add_friend/', views.add_friend, name='add_friend'),
    path('<str:username>/remove_friend/', views.remove_friend, name='remove_friend'),

    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/edit_post/', views.edit_post, name='edit_post'),

    path('<str:username>/news/', views.news_list, name='news'),
    path('<str:username>/like/', views.handle_like_view, name='handle_like'),

    path('<str:username>/subscribe/', views.subscribe, name='subscribe'),
    path('<str:username>/unsubscribe/', views.unsubscribe, name='unsubscribe'),
]