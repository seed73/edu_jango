# auth_app/keycloak_backend.py
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from jose import jwt
from decouple import config
from jose import jwt
from auth_app.models import Account, MyUser

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
            KEY_BEGIN = "-----BEGIN PUBLIC KEY-----"
            KEY_END = "-----END PUBLIC KEY-----"

            
            public_key = f"""{KEY_BEGIN}\n{config('KEYCLOAK_EDU_RELM_PUBLIC_KEY_RS256')}\n{KEY_END}"""
            token_json = jwt.decode(token, public_key, algorithms=['HS256', 'RS256'], audience='account')
            user_id = token_json.get('preferred_username', None)

            if user_id:
                user, _ = MyUser.objects.get_or_create(user_id=user_id, defaults={'first_name': 'Keycloak User'})
                return (user, token)
            return None

            # decoded_token = jwt.decode(token, key, algorithms=['RS256'])
            
            # 토큰이 유효하면 사용자 인증 및 필요한 정보 반환
            # ... 사용자 인증 로직
            # return (user, None)  # 인증 성공 시 사용자 객체와 None 반환
            return None

        except jwt.JWTError as e:
            raise exceptions.AuthenticationFailed('Token is invalid')

        except Exception as e:
            print(e)
            raise exceptions.AuthenticationFailed('Token could not be decoded')
