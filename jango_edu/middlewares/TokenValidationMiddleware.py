from jango_edu.utils.jwt_helper import validate_token

class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization', '').split('Bearer ')[-1]
        
        # Replace the following constants with appropriate values
        JWKS_URL = "http://localhost:8080/auth/realms/edu/protocol/openid-connect/certs"
        AUDIENCE = "eduplex_account"
        ISSUER = "http://localhost:8080/auth/realms/edu"

        try:
            payload = validate_token(token, JWKS_URL, AUDIENCE, ISSUER)
            request.user_payload = payload
        except Exception as e:
            # Handle the exception. For example, you can set a 401 status on the response
            pass

        response = self.get_response(request)
        return response