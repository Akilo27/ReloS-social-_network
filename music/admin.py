from django.contrib import admin
from .models import Song,ProfileSong


admin.site.register(ProfileSong)
admin.site.register(Song)