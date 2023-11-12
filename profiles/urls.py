
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/edit_post/', views.edit_post, name='edit_post'),
    path('<str:username>/news/', views.news_list, name='news'),
    path('<str:username>/like/', views.handle_like_view, name='handle_like'),
]
