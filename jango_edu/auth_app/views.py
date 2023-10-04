from rest_framework import generics, status
from .models import Account
from .serializers import AccountSerializer
import requests
from rest_framework.response import Response
from decouple import config
from utils.logger import get_logger

logger = get_logger()

class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']

        # Keycloak Admin API에 회원가입 요청
        keycloak_host = config('KEYCLOAK_HOST')
        keycloak_id = config('KEYCLOAK_ID')
        keycloak_realm = config('KEYCLOAK_REALM')
        keycloak_pass = config('KEYCLOAK_PASS')
        keycloak_client_id = config('KEYCLOAK_CLIENT_ID')
        keycloak_secret = config('KEYCLOAK_SECRET')

        admin_token_url = f"{keycloak_host}/auth/realms/{keycloak_realm}/protocol/openid-connect/token"
        admin_users_url = f"{keycloak_host}/auth/admin/realms/{keycloak_realm}/users"

        # 관리자 토큰 가져오기
        admin_data = {
            "grant_type": "password",
            "client_id": keycloak_client_id,
            "client_secret": keycloak_secret,
            "username": keycloak_id,
            "password": keycloak_pass
        }
        token_response = requests.post(admin_token_url, data=admin_data)

        if token_response.status_code != 200:
            logger.info(token_response)
            logger.info(f"Token Response from Keycloak: {token_response.status_code} - {token_response.text}")
            return Response({"error": "Cannot get admin token"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        access_token = token_response.json()["access_token"]

        # 사용자 추가
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        user_info = {
            "username": serializer.validated_data['name'],
            "enabled": True,
            "emailVerified": True,  # 필요에 따라 변경
            "email": serializer.validated_data['email'],
            "credentials": [{"type": "password", "value": password, "temporary": False}]
        }
        user_response = requests.post(admin_users_url, json=user_info, headers=headers)

        if user_response.status_code != 201:
            logger.info(f"Response from Keycloak: {user_response.status_code} - {user_response.text}")
            return Response({"error": "Cannot create user in Keycloak"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return super().post(request, *args, **kwargs)