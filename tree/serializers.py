from rest_framework import serializers

from .models import Type, Trees
from users.serializers import UserSerializer


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = (
            "id",
            "name",
        )


class TreesSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    user = UserSerializer()

    class Meta:
        model = Trees
        fields = (
            "id",
            "user",
            "name",
            "type",
            "image",
            "definition",
            "latitude",
            "longitude",
            "is_verified",
        )

