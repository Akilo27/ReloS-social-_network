
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/edit_post/', views.edit_post, name='edit_post'),
]