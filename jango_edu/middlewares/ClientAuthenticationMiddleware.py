from django.http import JsonResponse

class ClientAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 클라이언트 ID와 시크릿 추출
        authorization = request.headers.get('Authorization')
        # client_secret = request.headers.get('X-Client-Secret')

        # 인증 로직
        if not self.validate_client(authorization):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

    def validate_client(self, authorization):
        print('1111111111111')
        print(authorization)
        # 여기에 클라이언트 인증 로직 구현
        # 예: 데이터베이스에 저장된 ID와 시크릿을 확인
        return True  # 임시로 항상 True 반환