from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('id', 'user_id', 'name', 'phone_number', 'gender', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}