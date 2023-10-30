from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from decouple import config
import hashlib

# 환경변수로부터 비밀 키를 불러옵니다.
SECRET_KEY = config('AES256_SECRET_KEY')

def get_aes_cipher():
    key = hashlib.sha256(SECRET_KEY.encode()).digest()
    # 초기화 벡터(IV)는 16바이트 길이여야 합니다.
    # 실제 운영 환경에서는 IV를 암호화에 사용할 때마다 저장하고 관리해야 합니다.
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher

def encrypt_data(plain_text):
    cipher = get_aes_cipher()
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_text)
    encrypted_text = b64encode(cipher.iv + encrypted_bytes).decode('utf-8')
    return encrypted_text

def decrypt_data(encrypted_text):
    encrypted_data = b64decode(encrypted_text)
    iv = encrypted_data[:AES.block_size]
    encrypted_data_bytes = encrypted_data[AES.block_size:]
    cipher = AES.new(hashlib.sha256(SECRET_KEY.encode()).digest(), AES.MODE_CBC, iv)
    padded_text = cipher.decrypt(encrypted_data_bytes)
    plain_text = unpad(padded_text, AES.block_size).decode('utf-8')
    return plain_text