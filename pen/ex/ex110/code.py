import base64

original_string = "KEY019-8Dqc_a!uET`CBBKdr@@dd\x0\en"

# Encode the string using Base64
encoded_bytes = base64.b64encode(original_string.encode())
encoded_string = encoded_bytes.decode()

# Replace characters to match the desired format
final_string = encoded_string.replace('+', '-').replace('/', '_').replace('=', '')

# Add the prefix
final_string = f"KEY019-{final_string}=="

print(final_string)

