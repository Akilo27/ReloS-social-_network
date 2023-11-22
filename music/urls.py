from django.urls import path
from .views import song_list, song_upload, music_user, add_for_user_song, delete_song

app_name = 'music'

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('upload/', song_upload, name='song_upload'),
    path('user/', music_user, name='music_user'),
    path('user_add/<int:i>/', add_for_user_song, name='add_user_song'),
    path('user_delete/<int:i>/', delete_song, name='delete_user_song'),
]
