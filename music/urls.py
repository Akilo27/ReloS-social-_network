from django.urls import path
from .views import song_list, song_upload

app_name = 'music'

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('upload/', song_upload, name='song_upload'),
]