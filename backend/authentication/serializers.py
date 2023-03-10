from rest_framework import serializers

from .models import User


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username',
            'email',
            'password', 
            'first_name', 
            'last_name',
            'iban'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'iban',
            'first_name',
            'last_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = (
            'id',
        )
