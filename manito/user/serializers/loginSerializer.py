from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'password'
        ]

        read_only_fields = [
            'name',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
