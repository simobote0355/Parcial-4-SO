from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_filename="secret.key"):
    with open(key_filename, "wb") as key_file:
        key_file.write(key)

def load_key(key_filename="secret.key"):
    with open(key_filename, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)