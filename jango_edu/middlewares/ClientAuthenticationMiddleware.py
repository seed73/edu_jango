from django.http import JsonResponse
from utils.crypto import decode_base64
from decouple import config

# 사실 미들웨어 안써도 되고 login에 직접 넣는게 좋은데 그냥 미들웨어 써볼겸 해서 써봄

class ClientAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 로그인 일때만
        if request.path == '/api/login/':
            # 클라이언트 ID와 시크릿 추출
            authorization = request.headers.get('LoginAuthorization')
            if not self.validate_client(authorization):
                return JsonResponse({'error': 'Unauthorized'}, status=401)    
        response = self.get_response(request)
        return response

    def validate_client(self, authorization):
        try:
            _front_id = config("REACT_APP_EDU_FRONT_ID")
            _front_secret = config("REACT_APP_EDU_FRONT_CLIENT_SECRET")
            if decode_base64(authorization) == f'Basic {_front_id} {_front_secret}':
                return True  # 임시로 항상 True 반환
            else:
                return False
        except:
            return False