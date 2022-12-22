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


class TreeSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    user = UserSerializer()

    class Meta:
        model = Trees
        fields = (
            "id",
            "user",
            "name",
            "type",
            "get_image",
            "get_qrcode",
            "definition",
            "latitude",
            "longitude",
            'created_at',
            "is_verified",
        )


class TreeCreateSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all(), source="type", write_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Trees
        fields = (
            "user",
            "name",
            "type",
            "type_id",
            "image",
            "definition",
            "latitude",
            "longitude",
            "is_verified",
        )
