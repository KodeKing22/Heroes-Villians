from itertools import product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperTypes
from .serializers import SuperTypesSerializer


@api_view(['GET', 'POST'])
def supertype_list(request):
    if request.method == 'GET':
        supertypes = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(supertypes, two=True)
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


