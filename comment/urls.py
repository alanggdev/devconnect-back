from django.urls import path

from .views import get_all_comments, create_comment, get_detail_comment, delete_comment, update_comment, get_post_comments, get_user_comments

urlpatterns = [
    path('list', get_all_comments, name='list-comment'),
    path('create', create_comment, name='create-comment'),
    path('detail/<int:id>', get_detail_comment, name='detail-comment'),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
    path('update/<int:id>', update_comment, name='update-comment'),
    path('post/<int:post_id>', get_post_comments, name='post-comment'),
    path('user/<int:user_id>', get_user_comments, name='user-comment'),
]