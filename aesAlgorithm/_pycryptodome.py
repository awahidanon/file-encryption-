from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os

# AES-256 key size
KEY_SIZE = 32
BLOCK_SIZE = AES.block_size  # AES block size for CBC mode (16 bytes)

def generate_key(password: bytes, salt: bytes) -> bytes:
    # Derive a 256-bit key from the password and salt using PBKDF2
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=100000)

def encrypt_file(input_file: str, output_file: str, password: bytes):
    # Generate a random salt and initialization vector (IV)
    salt = get_random_bytes(16)
    iv = get_random_bytes(BLOCK_SIZE)
    
    # Derive key from password and salt
    key = generate_key(password, salt)
    
    # Create cipher object with AES-256 in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Open the input and output files
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        # Write the salt and IV to the output file
        f_out.write(salt)
        f_out.write(iv)
        
        # Encrypt file data with padding
        while chunk := f_in.read(1024):
            # Pad chunk if it's not a full block
            if len(chunk) % BLOCK_SIZE != 0:
                padding_length = BLOCK_SIZE - len(chunk) % BLOCK_SIZE
                chunk += bytes([padding_length] * padding_length)
            encrypted_data = cipher.encrypt(chunk)
            f_out.write(encrypted_data)
        
        # If the last chunk was a full block, add padding to meet AES requirements
        if len(chunk) % BLOCK_SIZE == 0:
            padding_length = BLOCK_SIZE
            f_out.write(cipher.encrypt(bytes([padding_length] * padding_length)))
        print("ecrypted sucessfully")     
def decrypt_file(input_file: str, output_file: str, password: bytes):
    # Read the salt and IV from the input file
    with open(input_file, 'rb') as f_in:
        salt = f_in.read(16)
        iv = f_in.read(BLOCK_SIZE)
        
        # Derive key from password and salt
        key = generate_key(password, salt)
        
        # Create cipher object with AES-256 in CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt file data
        with open(output_file, 'wb') as f_out:
            while chunk := f_in.read(1024):
                decrypted_data = cipher.decrypt(chunk)
                
                # Remove padding if this is the last chunk
                if len(chunk) < 1024:
                    padding_length = decrypted_data[-1]
                    decrypted_data = decrypted_data[:-padding_length]
                    
                f_out.write(decrypted_data)
            print("decrypted sucessfully")
 
password = b"12345678"  # Use a secure password
encrypt_file("/workspaces/file-encryption-/AES-256/image.png", "/workspaces/file-encryption-/AES-256/encrypted.bin", password)
decrypt_file("/workspaces/file-encryption-/AES-256/encrypted.bin", "/workspaces/file-encryption-/AES-256/image.png", password)
