from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from .models import CommentModel
from .serializers import CommentSerializer

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

def search_comment(post_id):
    try:
        return CommentModel.objects.get(pk = post_id)  
    except CommentModel.DoesNotExist:   
        return 0
    
@api_view(['GET'])
def get_all_comments(request):
    queryset = CommentModel.objects.all()
    serializer = CommentSerializer(queryset, many=True ,context={'request':request})
    return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))

@api_view(['POST'])
def create_comment(request, *args, **kwargs):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(custom_response("Created", serializer.data, status=status.HTTP_201_CREATED))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

@api_view(['GET'])
def get_detail_comment(request, id, format=None):
    comment = search_comment(id)
    if comment != 0:
        serializer = CommentSerializer(comment)
        return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['DELETE'])
def delete_comment(request, id, format = None):
    objetive = search_comment(id)
    if objetive != 0:
        objetive.delete()
        return Response(custom_response("Success", "Deleted", status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['PATCH'])
def update_comment(request, id, format=None):
    objetive = search_comment(id)
    serializer = CommentSerializer(objetive, data=request.data)
    if serializer.is_valid() and objetive != 0:
        serializer.save()
        return Response(custom_response("Updated", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_404_NOT_FOUND))

@api_view(['GET'])
def get_user_comments(request, user_id, format=None):
    posts = CommentModel.objects.filter(author=user_id)
    if len(posts) != 0:
        serializer = CommentSerializer(posts, many=True, context={'request': request})
        return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

@api_view(['GET'])
def get_post_comments(request, post_id, format=None):
    posts = CommentModel.objects.filter(post_comment=post_id)
    if len(posts) != 0:
        serializer = CommentSerializer(posts, many=True, context={'request': request})
        return Response(custom_response("Success", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))

