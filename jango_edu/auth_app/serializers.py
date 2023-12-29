from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('id', 'user_id', 'name', 'phone_number', 'entering_date', 'gender', 'email', 'password','position')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        return super().create(validated_data)