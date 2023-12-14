#!/usr/bin/python3

def xor_bytes(data, key):
    result = bytes(x ^ y for x, y in zip(data, key))
    return result

input_string = b"8Dqc_a!uE\x7fT`CBBKdr@@dd\x0e\n"
byte = b'\x13\x33\x37'
byte = byte * 8
print("XOR Result:", xor_bytes(input_string, byte))

