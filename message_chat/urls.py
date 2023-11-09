from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/>', views.messages, name='message_chat'),
]
