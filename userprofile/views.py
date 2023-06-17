from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import UserProfileModel
from .serializers import UserProfileSerializer, UserProfileSerializerModificate

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

def search_userprofile(pk):
    try:
        return UserProfileModel.objects.get(pk = pk)  
    except UserProfileModel.DoesNotExist:   
        return 0

@api_view(['GET'])
def get_all_userproiles(request):
    queryset = UserProfileModel.objects.all()
    serializer = UserProfileSerializer(queryset, many=True ,context={'request':request})
    return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))

@api_view(['POST'])
def create_userprofile(request, *args, **kwargs):
    serializer = UserProfileSerializerModificate(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(custom_response("Created", serializer.data, status=status.HTTP_201_CREATED))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

@api_view(['GET'])
def get_detail_userprofile(request, id, format=None):
    userprofile = search_userprofile(id)
    if userprofile != 0:
        serializer = UserProfileSerializer(userprofile)
        return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['PATCH'])
def update_userprofile(request, id, format=None):
    userprofile = search_userprofile(id)
    serializer = UserProfileSerializerModificate(userprofile, data=request.data)
    if serializer.is_valid():
        # userprofile.user_avatar.delete(save=True)
        # userprofile.user_backgroud.delete(save=True)
        serializer.save()
        return Response(custom_response("Updated", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_404_NOT_FOUND))

@api_view(['GET'])
def get_user_userprofile(request, user_id, format=None):
    try:
        userprofile = UserProfileModel.objects.get(user_profile=user_id)
    except UserProfileModel.DoesNotExist:
        return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
    
    serializer = UserProfileSerializer(userprofile, context={'request': request})
    return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
