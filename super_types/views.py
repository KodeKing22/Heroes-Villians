from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers import serializers
from .serializers import SuperTypesSerializer
from .models import SuperTypes


@api_view(['GET', 'POST'])
def supertype_list(request):
    if request.method == 'GET':
        supertypes = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(supertypes, two=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = SuperTypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def supertype_detail(request, pk):
    supertypes = get_object_or_404(SuperTypes, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(supertypes)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(supertypes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supertypes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def super_type_list(request):
    if request.method == 'GET':
       request.query_params.get(type=hero)
       

    return Response()

