from cryptography.fernet import Fernet

message = "hello"
key = "1234567"

fernet = Fernet(f"{key * 6}w=")
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# encMessage = b'gAAAAABhk9ET472OKhgb0uNhUA-kAITT_sAjDrVf1GYowT-EoaoO-HZ0lX2XdIhqnHq-KmLmv6RpTnUwIDp9jKcTmcR8v-S21A=='

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
