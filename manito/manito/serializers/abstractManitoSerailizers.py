from rest_framework import serializers

from manito.models import Manito
from user.serializers import UserSerializer


class AbstractManitoSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Manito
        fields = [
            'id',
            'title',
            'author',
            'type',
            'created_at',
            'end_at'
        ]

        read_only_fields = [
            'id',
            'title',
            'author'
            'type',
            'created_at',
            'end_at',
        ]
