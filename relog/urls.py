from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/edit_post/', views.edit_post, name='edit_post')
]
