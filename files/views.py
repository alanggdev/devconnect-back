from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

from files.models import FileModel
from files.serializers import FileSerializer

def custom_response(msg, response, status):
    data ={
        "message": msg,
        "pay_load": response,
        "status": status,
    }
    res= json.dumps(data)
    response = json.loads(res)
    return response

def search_post(file_id):
    try:
        return FileModel.objects.get(pk = file_id)  
    except FileModel.DoesNotExist:   
        return 0

@api_view(['GET'])
def get_all_files(request):
    queryset = FileModel.objects.all()
    serializer = FileSerializer(queryset, many=True ,context={'request':request})
    return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))

@api_view(['POST'])
def create_file(request, *args, **kwargs):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(custom_response("Created", serializer.data, status=status.HTTP_201_CREATED))
    return Response(custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

@api_view(['GET'])
def get_detail_file(request, id, format=None):
    file_searched = search_post(id)
    if file_searched != 0:
        serializer = FileSerializer(file_searched)
        return Response(custom_response("Returned", serializer.data, status=status.HTTP_200_OK))
    return Response(custom_response("Error", "Not found", status=status.HTTP_404_NOT_FOUND))


    
