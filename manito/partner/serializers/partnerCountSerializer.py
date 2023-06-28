from partner.models import Partner
from rest_framework import serializers


class PartnerCountSerializer(serializers.ModelSerializer):
    total_count = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'total_count',
        ]

    def get_total_count(self, obj):
        return obj.total_count
