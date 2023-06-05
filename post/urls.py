from django.urls import path

from .views import get_all_posts, create_post, get_detail_post, update_post, get_user_posts, delete_post

urlpatterns = [
    path('list', get_all_posts, name='list-post'),
    path('create', create_post, name='create-post'),
    path('delete/<int:id>', delete_post, name='delete-post'),
    path('detail/<int:id>', get_detail_post, name='detail-post'),
    path('update/<int:id>', update_post, name='update-post'),
    path('user/<int:user_id>', get_user_posts, name='user-post'),
]