from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.chat, name='chats'),
    path('chat/<str:username>/',views.dialog, name='messages'),
]
