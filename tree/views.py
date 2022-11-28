from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trees
from .serializers import TreesSerializer
# Create your views here.


class TreeListApiView(APIView):
    def get(self, request, format=None):
        trees = Trees.objects.all()
        serializer = TreesSerializer(trees, many=True)
        return Response(serializer.data)


class TreeDetailApiView(APIView):
    def get(self, request, id):
        tree = Trees.objects.get(id=id)
        serializer = TreesSerializer(tree)
        return Response(serializer.data)