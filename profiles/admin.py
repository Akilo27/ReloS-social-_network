from django.contrib import admin
from .models import UserProfile, BlogUser


admin.site.register(UserProfile)
admin.site.register(BlogUser)