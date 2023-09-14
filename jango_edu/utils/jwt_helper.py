import jwt
import requests


def validate_token(token, jwks_url, audience, issuer):
    """
    Validates a JWT token against the provided jwks, audience, and issuer.
    
    :param token: The JWT token to validate.
    :param jwks_url: The URL to fetch the JWKS (JSON Web Key Set) for token validation.
    :param audience: The expected audience (aud claim) of the token.
    :param issuer: The expected issuer (iss claim) of the token.
    :return: The token payload if valid, otherwise raises an exception.
    """

    # Fetch the JWKS
    jwks = requests.get(jwks_url).json()
    
    # Decode the token header
    headers = jwt.get_unverified_header(token)
    
    # Find the appropriate key
    rsa_key = {}
    for key in jwks['keys']:
        if key['kid'] == headers['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e'],
            }
    
    # If we have the key, attempt to decode and validate the token
    if rsa_key:
        payload = jwt.decode(
            token,
            key=rsa_key,
            algorithms=['RS256'],
            audience=audience,
            issuer=issuer
        )
        return payload
    else:
        raise Exception("Unable to locate appropriate key for this token.")

# Usage example:

token = "YOUR_JWT_TOKEN_HERE"
jwks_url = "https://YOUR_KEYCLOAK_DOMAIN/auth/realms/YOUR_REALM/protocol/openid-connect/certs"
audience = "YOUR_CLIENT_ID"  # Usually the client_id
issuer = "https://YOUR_KEYCLOAK_DOMAIN/auth/realms/YOUR_REALM"

try:
    payload = validate_token(token, jwks_url, audience, issuer)
    print("Token is valid. Payload:", payload)
except Exception as e:
    print("Token validation failed:", e)