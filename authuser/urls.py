from django.urls import include, path
from .views import search_username

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('search/<str:username>', search_username, name='search-usernames'),
]