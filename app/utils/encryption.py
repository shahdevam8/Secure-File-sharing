from cryptography.fernet import Fernet

def encrypt(data):
    key = Fernet.generate_key()
    return Fernet(key).encrypt(data), key

def decrypt(data, key):
    return Fernet(key).decrypt(data)
