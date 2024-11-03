from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# AES-256 key size
KEY_SIZE = 32
BLOCK_SIZE = 16  # AES block size for CBC mode (128 bits)

def generate_key(password: bytes, salt: bytes):
    # Derive a 256-bit key from the password and salt using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt_file(input_file: str, output_file: str, password: bytes):
    # Generate a random salt and initialization vector (IV)
    salt = os.urandom(16)
    iv = os.urandom(BLOCK_SIZE)
    
    # Derive key from password and salt
    key = generate_key(password, salt)
    
    # Create cipher object with AES-256 in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Open the input and output files
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        # Write the salt and IV to the output file
        f_out.write(salt)
        f_out.write(iv)
        
        # Initialize padding for AES CBC mode
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        
        # Encrypt file data
        while chunk := f_in.read(1024):
            padded_data = padder.update(chunk)
            encrypted_data = encryptor.update(padded_data)
            f_out.write(encrypted_data)
        
        # Finalize padding and encryption
        padded_data = padder.finalize()
        f_out.write(encryptor.update(padded_data) + encryptor.finalize())
        print("encrypted sucessfully")

def decrypt_file(input_file: str, output_file: str, password: bytes):
    # Read the salt and IV from the input file
    with open(input_file, 'rb') as f_in:
        salt = f_in.read(16)
        iv = f_in.read(BLOCK_SIZE)
        
        # Derive key from password and salt
        key = generate_key(password, salt)
        
        # Create cipher object with AES-256 in CBC mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Initialize unpadding for AES CBC mode
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        
        # Decrypt file data
        with open(output_file, 'wb') as f_out:
            while chunk := f_in.read(1024):
                decrypted_data = decryptor.update(chunk)
                unpadded_data = unpadder.update(decrypted_data)
                f_out.write(unpadded_data)
            
            # Finalize decryption and unpadding
            decrypted_data = decryptor.finalize()
            f_out.write(unpadder.update(decrypted_data) + unpadder.finalize())
            print("decrypted sucessfully")

password = b"12345678"  # Use a secure password
encrypt_file("/workspaces/file-encryption-/AES-256/image.png", "/workspaces/file-encryption-/AES-256/encrypted.bin", password)
decrypt_file("/workspaces/file-encryption-/AES-256/encrypted.bin", "/workspaces/file-encryption-/AES-256/image.png", password)
