import binascii
import base64

# Hexadecimal string
hex_string = "cc"

# Step 1: Convert hexadecimal to binary
binary_data = binascii.unhexlify(hex_string)

# Step 2: Encode binary data to Base64
base64_data = base64.b64encode(binary_data).decode('utf-8')

# Print the Base64-encoded result
print("Hexadecimal:", hex_string)
print("Base64:", base64_data)

