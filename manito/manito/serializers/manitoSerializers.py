from rest_framework import serializers

from manito.models import Manito
from user.serializers import UserSerializer


class ManitoSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Manito
        fields = [
            'id',
            'title',
            'content',
            'author',
            'type',
            'price',
            'mail_data',
            'name_data',
            'created_at',
            'end_at'
        ]

        read_only_fields = [
            'id',
            'author'
            'created_at',
        ]
