#!/usr/bin/python3

from Crypto.Cipher import AES
from base64 import b64decode, b64encode

BLOCK_SIZE = 16
PADDING = b'{'

'''def pad(s):
    return s + ((BLOCK_SIZE - len(s)) % BLOCK_SIZE) * PADDING'''


def decryptKey(iv, key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    res = cipher.decrypt(ciphertext)
    return res

keys = [
b'VGhlcmUgaXMgbm8ga2V5Lg==',
b'HcIGRLxTkUEkQVENTLN3zA==',
b'u+9loQ38tAbuRzJbIHcKpQ==',
b'vSS4f8194m2vZhxbxKy3jg==',
b'X1oCUHUnVMX9kbG16Wtdxw==',
b'hKku4/qTxNsmJIG0iT8pSQ==',
b'LHQ0LWLBEE1FnwPr9clv5A==',
b'52kyxvjHNa8SNF/s55JH0A==',
b'u35DuEmIe319ItByiKdK/Q==',
b'qXwMWFqWcPnd6l1oMoCtFw==',
b'OSQWWfy+0dDoux+fU3poNQ==',
b'0V/RiTD2g6UDXg8SosE1CQ==',
b'uQC1WMZMFC9syMdne+o0pA==',
b'Hdco+146WmFI8AfAxeFEvQ==',
b'Ea0alCyO8It7TqmQNMWPcQ==',
b'jXuPkMr5V3Fv2LsQFMLC2w==',
b'g+XS/JPvCaodk22fqu6zPw==',
b'5iJXxl+AoPQqKssw3WJUnw==',
b'1aFulon4qe/Hi18bjbCPlw==',
b'+wFplV2FrlgWPquXWESsSw==',
b'yaKtbDTPSfRA66tlV0CyPw==',
b'hx/+Xlvu9RRMPDMNe7ApBQ==',
b'uidv+ycMuQwy9xQ0MSlHCQ==',
b'MtgK8PWxXRmCLrfDD38NxQ==',
]


if __name__ == "__main__":
    iv = b'\xe3T\x1cJA\xc1fHx\x99\xf5Hq\xcb\x0f\xf3'
    key = b'There is no key.'
    ciphertext =  b''.join(b64decode(encoded_key) for encoded_key in keys)
    plaintext = decryptKey(iv, key, ciphertext)
    print("Plain Text:", plaintext.decode('ISO-8859-1'))
