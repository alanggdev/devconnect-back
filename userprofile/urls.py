from django.urls import path

from .views import get_all_userproiles, create_userprofile, get_detail_userprofile, update_userprofile, get_user_userprofile, get_user_userprofile_simple

urlpatterns = [
    path('list/', get_all_userproiles, name='list-usersprofile'),
    path('create/', create_userprofile, name='create-usersprofile'),
    path('detail/<int:id>', get_detail_userprofile, name='detail-usersprofile'),
    path('update/<int:id>', update_userprofile, name='update-usersprofile'),
    path('user/<int:user_id>', get_user_userprofile, name='user-usersprofile'),
    path('user/simple/<int:user_id>', get_user_userprofile_simple, name='user-usersprofile-simple'),
]