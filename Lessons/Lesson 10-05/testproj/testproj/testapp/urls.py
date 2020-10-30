from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>', views.post, name='post')
]
