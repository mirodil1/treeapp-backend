from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Trees
from .serializers import TreeSerializer
# Create your views here.


class TreeListApiView(APIView):
    def get(self, request, format=None):
        trees = Trees.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)


class TreeDetailApiView(APIView):
    def get(self, request, id):
        tree = Trees.objects.get(id=id)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)


class UsersTree(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trees = Trees.objects.filter(user=request.user)
        serializer = TreeSerializer(trees, many=True)
        print(serializer.data)
        return Response(serializer.data)