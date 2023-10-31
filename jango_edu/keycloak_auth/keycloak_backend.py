# auth_app/keycloak_backend.py
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from jose import jwt
from django.conf import settings

class KeycloakBackend(BaseAuthentication):
    def authenticate(self, request):
        # HTTP_AUTHORIZATION 헤더에서 토큰 가져오기
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None
        
        # 헤더에서 토큰 분리
        prefix, token = auth_header.split(' ')
        if prefix.lower() != 'bearer':
            raise exceptions.AuthenticationFailed('Bearer schema not used')
        
        # 토큰 검증 로직
        try:
            # Keycloak public key 또는 secret key를 이용해 토큰 검증
            key = settings.KEYCLOAK_PUBLIC_KEY  # 예시로 설정에서 가져옴
            decoded_token = jwt.decode(token, key, algorithms=['RS256'])
            
            # 토큰이 유효하면 사용자 인증 및 필요한 정보 반환
            # ... 사용자 인증 로직
            return (user, None)  # 인증 성공 시 사용자 객체와 None 반환

        except jwt.JWTError as e:
            raise exceptions.AuthenticationFailed('Token is invalid')

        except Exception as e:
            raise exceptions.AuthenticationFailed('Token could not be decoded')

    def authenticate_header(self, request):
        return 'Bearer'