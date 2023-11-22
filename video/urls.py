from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('add/', views.video_add, name='video_add'),
    path('user/', views.user_video, name='user_video'),
    path('user_add/<int:i>/', views.add_for_user_video, name='add_user_video'),
    path('user_delete/<int:i>/', views.delete_video, name='delete_user_video'),
]