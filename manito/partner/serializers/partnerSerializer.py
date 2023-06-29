from rest_framework import serializers

from partner.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'manito',
            'manito_sender',
            'manito_receiver',
        ]
