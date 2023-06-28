from rest_framework import serializers

from manito.models import Manito


class ManitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manito
        fields = [
            'id',
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
            'created_at',
        ]
