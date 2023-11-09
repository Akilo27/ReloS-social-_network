from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
