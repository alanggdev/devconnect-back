from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json
from userprofile.models import UserProfileModel
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response


@api_view(['GET'])
def search_username(request, username, format=None):
    users = User.objects.filter(username__icontains=username)
    data = []
    for user in users:
        profile = UserProfileModel.objects.get(user_profile=user.pk)
        user_data = {
            'pk': user.pk,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile': {
                'avatar': profile.user_avatar.url if profile.user_avatar else None,
            }
        }
        data.append(user_data)
    return Response(data)