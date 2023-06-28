from partner.models import Partner
from rest_framework import serializers


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'manito',
            'manito_sender',
            'manito_receiver',
        ]
