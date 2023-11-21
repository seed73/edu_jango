from django.http import JsonResponse
from utils.crypto import encrypt_data, decrypt_data, decode_base64
from decouple import config

class ClientAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 클라이언트 ID와 시크릿 추출
        authorization = request.headers.get('Authorization')

        # 인증 로직
        if not self.validate_client(authorization):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

    def validate_client(self, authorization):
        print(decode_base64(authorization))
        SECRET_KEY = config('AES256_SECRET_KEY')
        if authorization == 'Basic dbrkdgmlWkdWkdaos 2ff3e2db21a9ba8a9d430d1167fdf015db14bde40cefc66cc83ff978cfb36380':
            # 여기에 클라이언트 인증 로직 구현
            # 예: 데이터베이스에 저장된 ID와 시크릿을 확인
            return True  # 임시로 항상 True 반환
        else:
            return False