from django.urls import path
from .views import community_list, create_community, edit_community

app_name = 'community'

urlpatterns = [
    path('', community_list, name='community_list'),
    path('create/', create_community, name='create_community'),
    path('edit/<int:community_id>/', edit_community, name='edit_community'),
]
