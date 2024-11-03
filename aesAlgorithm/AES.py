# steps the formula
#inital data and key 
# 2.Add round key 
# 3 .sub bytes 
# 4. shift row 
# 5. mix coloum  
# 6. final round

# example formula
# 1. input matrix  sampleMatrix= [0x00, 0x10, 0x20, 0x30]
 ##                       [0x44, 0x55, 0x66, 0x77]
  #                       [0x88, 0x99, 0xAA, 0xBB]
  #                       [0x16, 0xEE, 0x23, 0x30]
  #                       

#2. flatten the matrix
    #Convert sampleMatrix to a one-dimensional byte array.
    #sampleMatrix_bytes=[0x00,0x10,0x20,0x30,0x44,0x55,0x66,0x77,0x88,0x99,0xAA,0xBB,0x16,0xEE,0x23,0x30]

#3.  Padding
#          padded_text=pad(sampleMatrix_bytes,16) 

#4. Generate IV 
        # Create a random Initialization Vector (IV)
        #iv=os.urandom(16)

#5. Create Cipher Object
          #Use AES in CBC mode with the key and IV.
          #  cipher=AES.new(key, AES.MODE_CBC, iv)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import numpy as np
import os

def gKey():
    # generate a random 256-bit key for AES-256
    return os.urandom(32)  

def encrypt(sampleMatrix, key):
    # generate a random 16-byte IV
    iv = os.urandom(16)  # iv =  random 16-byte IV is generated
    
    # initializes the cipher with the provided key and IV in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Flatten the sampleMatrix matrix and convert to bytes
    sampleMatrix_bytes = sampleMatrix.flatten().tobytes()
    
    # pad the plaintext and block size
    padded_text = pad(sampleMatrix_bytes, AES.block_size)
    # encrypt the padded plaintext
    cipher_text = cipher.encrypt(padded_text)
    
    # return the Intial vector and the cipher text
    return iv + cipher_text

def decrypt(cipher_text, key):
    # extract the IV from the beginning of the cipher text
    iv = cipher_text[:16]
    actual_cipher_text = cipher_text[16:]
    
    # Create a Cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv) #CBC = (Cipher Block Chaining)
    
    # decrypt the cipher text
    padded_plain_text = cipher.decrypt(actual_cipher_text)

    # Unpad the decrypted text
    plain_text = unpad(padded_plain_text, AES.block_size)
    
    return plain_text

# 
if __name__ == "__main__":
    # generate a key here
    key = gKey()
    
    # Sample sampleMatrix matrix (4x4)
    sampleMatrix = np.array([[0x00, 0x10, 0x20, 0x30],
                      [0x44, 0x55, 0x66, 0x77],
                      [0x88, 0x99, 0xAA, 0xBB],
                      [0x16, 0xEE, 0x23, 0x30],
                      [0xCC, 0xDD, 0xEE, 0xFF]], 
                      dtype=np.uint8)

    print("Initial state matrix:", sampleMatrix)

    # encryption  out put
    encrypted = encrypt(sampleMatrix, key)
    print("Encrypted results:", encrypted.hex())

    # decryption out put 
    decrypted = decrypt(encrypted, key)
    print("Decrypted results:", decrypted)
   

#    final out put
# Initial sample  matrix: [[  0  16  32  48]
#  [ 68  85 102 119]
#  [136 153 170 187]
#  [ 22 238  35  48]
#  [204 221 238 255]]
# Encrypted results: 56870257b09733e0b7b8d467b0a6c0c4ff8b4be6137e1f1c78339e9eba5fb70dd2023fd1df5461e674ca28014b70f432
# Decrypted results: b'\x00\x10 0DUfw\x88\x99\xaa\xbb\x16\xee#0\xcc\xdd\xee\xff'

# [Done] exited with code=0 in 0.256 seconds
