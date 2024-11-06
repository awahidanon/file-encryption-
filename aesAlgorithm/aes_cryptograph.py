

from cryptography.fernet import Fernet

# generate a key
def generate_key():
    return Fernet.generate_key()

# encrypt a file
def encrypt_file(fpath, key):
    fernet = Fernet(key)
    with open(fpath, 'rb') as file:
        file_data = file.read()  # Read the file data
    encrypted_data = fernet.encrypt(file_data)  # Encrypt the data
    with open(fpath + '.fernet.enc', 'wb') as file:
        file.write(encrypted_data)  # Write the encrypted data to a new file
    return encrypted_data

# decrypt a file
def decrypt_file(fpath, key):
    fernet = Fernet(key)
    with open(fpath, 'rb') as file:
        encrypted_data = file.read()  # Read the encrypted data
    decrypted_data = fernet.decrypt(encrypted_data) 
    with open(fpath + '.fernet.dec', 'wb') as file:
        file.write(decrypted_data)  # Write the decrypted data to a new file
    return decrypted_data

# File path
fpath = 'aesAlgorithm/mobile.csv'

# Key generation
key = generate_key()
print("the key:", key)
# Encryption
encrypted_data = encrypt_file(fpath, key)

# decryption
decrypted_data = decrypt_file(fpath + '.fernet.enc', key)
print("aes cryptograph token time")

# the out put
# [Running] python -u "c:\Users\Hp\Desktop\file-encryption-\aesAlgorithm\aes_cryptograph.py"
# the key: b'UTdDGQuETd--IfzL6v34w0mI-aY-B9A83yI1Cy7FPtk='
# aes cryptograph token time

# [Done] exited with code=0 in 0.144 seconds
