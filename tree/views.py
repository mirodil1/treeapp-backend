from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import permission_classes

from .models import Trees, Type
from .serializers import TypeSerializer, TreeSerializer, TreeCreateSerializer
# Create your views here.


class TreeTypeList(APIView):
    def get(self, format=None):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)


class TreeListApiView(APIView):
    def get(self, request, format=None):
        trees = Trees.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = TreeCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TreeDetailApiView(APIView):
    def get(self, request, id):
        tree = get_object_or_404(Trees, id=id)
        serializer = TreeSerializer(tree)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersTree(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trees = Trees.objects.filter(user=request.user).order_by('-created_at')
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)
