from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', community_list, name='community_list'),
    path('create/', create_community, name='create_community'),
    path('<str:name>/', community_detail, name='detail'),



    path('edit/<int:community_id>/', edit_community, name='edit_community'),
    path('create_blog/<int:community_id>/', create_post_community, name ='create_blog'),

    path('<str:username>/like/', handle_like_view, name='handle_like'),

]
