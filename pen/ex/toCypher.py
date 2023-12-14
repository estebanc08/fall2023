#!/usr/bin/python3

from Crypto.Cipher import AES
from base64 import b64decode, b64encode

iv = b'\xe3T\x1cJA\xc1fHx\x99\xf5Hq\xcb\x0f\xf3'
key = b'There is no key.'
text = b"You've gotten in! Let the games begin. Your task will become harder and harder as we proceed forward. You can decode key 009 by xoring with byte 0xf1 then use \"Ineffingvincible\" to decrypt the Ottendorf text found in web page .../cise.ufl.edu/~jnw/2023/Keys/tH3TXt.html. If you desire leeway credit on the final examination you need to provide the exact phrase given here (w/o quotati"
cipher = AES.new(key, AES.MODE_CBC, iv)
encoded = cipher.encrypt(text)
for i in range(0, len(text), 16):
    print(text[i:i+16], b64encode(encoded[i:i+16]))
