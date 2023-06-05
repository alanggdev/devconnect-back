from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import PostModel
from .serializers import PostSerializer

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

def search_post(post_id):
    try:
        return PostModel.objects.get(pk = post_id)  
    except PostModel.DoesNotExist:   
        return 0

@api_view(['GET'])
def get_all_posts(request):
    queryset = PostModel.objects.all()
    serializer = PostSerializer(queryset, many=True ,context={'request':request})
    return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))

@api_view(['POST'])
def create_post(request, *args, **kwargs):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(custom_response("Created", serializer.data, status=status.HTTP_201_CREATED))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

@api_view(['DELETE'])
def delete_post(request, id, format = None):
    objetive = search_post(id)
    if objetive != 0:
        objetive.delete()
        return Response(custom_response("Success", "Deleted", status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['GET'])
def get_detail_post(request, id, format=None):
    post = search_post(id)
    if post != 0:
        serializer = PostSerializer(post)
        return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['PATCH'])
def update_post(request, id, format=None):
    post = search_post(id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid() and post != 0:
        serializer.save()
        return Response(custom_response("Updated", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_404_NOT_FOUND))

@api_view(['GET'])
def get_user_posts(request, user_id, format=None):
    posts = PostModel.objects.filter(author=user_id)
    if len(posts) != 0:
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))
