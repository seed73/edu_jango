from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from utils.crypto import encrypt_data, decrypt_data
from rest_framework import serializers
from decouple import config
from rest_framework.permissions import AllowAny


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = decrypt_data(serializer.validated_data['username'])
        password = decrypt_data(serializer.validated_data['password'])
        
        token_url = config('KEYCLOAK_TOKEN_URL')    
        data = {
            'client_id': config('KEYCLOAK_CLIENT_ID'),
            'client_secret': config('KEYCLOAK_SECRET'),
            'grant_type': 'password',
            'username': username,
            'password': password,
        }
        response = requests.post(token_url, data=data)
        
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"error": "Invalid credentials", "return": response.json()}, status=status.HTTP_400_BAD_REQUEST)