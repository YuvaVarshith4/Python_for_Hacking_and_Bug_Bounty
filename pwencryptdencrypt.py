import base64

# def encryptpassword(password):
#     encoded_bytes = base64.b64encode(password.encode())
#     print(encoded_bytes)

def decrypt_password(encoded_password):
    decode_bytes = base64.b64decode(encoded_password)
    print(decode_bytes.decode())

# user_password = input("Enter your password: ")
# encryptpassword(user_password)
decrypt_password('eXV2YSB2YXJzaGl0aA==')
