from rest_framework import serializers

from ..models import Manito

class ManitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manito
        fields = {'author','type', 'price', 'mail_data', 'name_data', 'end_at'}