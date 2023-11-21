import os

# 32바이트 (256비트) 무작위 키를 생성합니다.
secret_key = os.urandom(32)

# 바이트를 16진수 문자열로 변환합니다.
hex_key = secret_key.hex()

print(secret_key)
print(hex_key)