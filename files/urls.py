from django.urls import path

from .views import get_all_files, get_detail_file, create_file

urlpatterns = [
    path('list', get_all_files, name='list-files'),
    path('create', create_file, name='create-files'),
    path('detail/<int:id>', get_detail_file, name='detail-files'),
]