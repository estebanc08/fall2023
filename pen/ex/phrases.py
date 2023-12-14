#!/usr/bin/python3

from Crypto.Cipher import AES
from base64 import b64decode, b64encode

BLOCK_SIZE = 16
PADDING = b'{'

def pad(s):
    return s + ((BLOCK_SIZE - len(s)) % BLOCK_SIZE) * PADDING

def decryptKey(iv, key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    res = cipher.decrypt(ciphertext)
    return res


iv = b'\x00'
iv = iv * 16
key = b'Ineffingvincible'
with open('binary', 'rb') as file:
    ciphertext = file.read()
plaintext = decryptKey(iv, key, ciphertext)
print(plaintext.decode('ISO-8859-1'))
