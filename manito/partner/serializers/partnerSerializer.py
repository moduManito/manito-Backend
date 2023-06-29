from partner.models import Partner
from rest_framework import serializers
from manito.serializers import AbstractManitoSerializer


class PartnerSerializer(serializers.ModelSerializer):
    manito = AbstractManitoSerializer(read_only=True)

    class Meta:
        model = Partner
        fields = [
            'id',
            'manito',
            'manito_sender',
            'manito_receiver',
        ]
