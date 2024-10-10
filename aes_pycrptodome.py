from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
 # this the encrypt file pycrptodome
def efp(fpath):
    key = get_random_bytes(16)   # the key sizes of 16 bytes = 128 bits,
    #24 bytes = 192 bits, or 32 bytes = 256 bits.
    cipher = AES.new(key, AES.MODE_CBC) #CBC = Cipher Block Chaining block of plaintext is combined (XORed)
    iv = cipher.iv  #initialization vector (iV) 
    with open(fpath, 'rb') as file:
        file_data = file.read()
    edata = cipher.encrypt(pad(file_data, AES.block_size))
    with open(fpath + '.aes.enc', 'wb') as file:  # the file is read by .aes.enc
        file.write(iv + edata)
    return key, iv, edata
# decrypt file pycrptodome
def dfp(fpath, key, iv, edata):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ddata = unpad(cipher.decrypt(edata), AES.block_size)
    with open(fpath + '.aes.dec', 'wb') as file:
        file.write(ddata)
    return ddata
# csv data loads
fpath = 'mobile.csv'

# Encryption
start_time = time.time()
key, iv, edata = efp(fpath)
end_time = time.time()
encryption_time_us = (end_time - start_time) * 1_000_000  # this is the Time in microseconds=(tend −tstart)×1,000,000 
print(f"encryption Time: {encryption_time_us:.2f} microseconds")

# Decryption
start_time = time.time()  # start time
ddata = dfp(fpath, key, iv, edata)
end_time = time.time() # end time
decryption_time_us = (end_time - start_time) * 1_000_000   # this is Time in microseconds=(tend −tstart)×1,000,000
print(f"decryption Time: {decryption_time_us:.2f} microseconds")




