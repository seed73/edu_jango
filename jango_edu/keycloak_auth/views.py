from django.http import JsonResponse
import requests

def login(request):
    # Frontend로부터 받은 자격 증명
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # Keycloak 인증 URL
    token_url = "http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/token"
    
    # Client 정보 (Keycloak에서 설정)
    client_id = "eduplex_account"
    client_secret = 'MIICrTCCAZUCBgGKQBO1ezANBgkqhkiG9w0BAQsFADAaMRgwFgYDVQQDDA9lZHVwbGV4X2FjY291bnQwHhcNMjMwODI5MDY1NDA4WhcNMzMwODI5MDY1NTQ4WjAaMRgwFgYDVQQDDA9lZHVwbGV4X2FjY291bnQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCGhVe7Gs6AMpcGVH4bmhGEwxC1J2aWt9/NUVGg9hUmKGNYtNhcY0ozYzA5zwJv6ZNHDUvwPENCpRKTdXRsN7pkF86FwenhkorKpa+x5ZdESMAbEgEH73eUZFgFj6NGyDjb+4g8VOpGDniR1DXcN5rcYNC97tAh7Iq5W5a6NRuoN7+KHejg96RdNIIa0Wx56kPCCrWQ0AQCyxLG+OtN+ptO+7e5lGdGd1Ow5MRqrrLLEWxaWZUeV6Y34foc9F9tnZ/PLtGmUJffUnB7c07zTuaEJ6Xd6ruqYx/EgPScZEs8yTWJhUbSXs0PHsJoQm0IZ8nOB/vR3kF9ev6pI9jLBpbpAgMBAAEwDQYJKoZIhvcNAQELBQADggEBACIhD3jRD68TNqXLE6N1VIwyuBxY3IyXY6t1ulq7gVWWsYEhtLnX1Ak1VbaZml9AmIVzW2eVYBHTOHV2OjusD8WQB2oUNZm97H1XzQO0BEr1sD1dMNi7LpgJUIV8M7b6k+Acfro+3zA0dKm/CL3j+/BTQ7NOCvDpzlDCbC4zg366WWRqbyBWWpHJi2c21JQHMbu6n7kwwIXIkaN+NB2g+QXUVySq4HDkbK+/A1wfsaohYxs25Se+rcdrRjqSVftH9aIECf9B1djS/G+qKmwm5lUVsYDoPEVmosFNKRIzK+aHrZZtOc5A7M51nV5UJT8AQkaBI9zk+5ZJyAF5Q71c2h0='
    
    # 토큰 요청
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        'username': username,
        'password': password,
    }
    response = requests.post(token_url, data=data)
    
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Invalid credentials","return":response.json()}, status=400)