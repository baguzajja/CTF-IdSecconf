from Crypto.Cipher import AES
import sys
import os
IV_SIZE = 16
BLOCK_SIZE = 16

key = sys.argv[1]

mode = AES.MODE_ECB
iv = os.urandom(IV_SIZE)
aes = AES.new(key, mode, iv)

with open(sys.argv[2], "rb") as f:
    data = f.read()

padding = BLOCK_SIZE - len(data) % BLOCK_SIZE

data += padding * "\x00"

encrypted = aes.encrypt(data)

with open(sys.argv[2] + ".encrypted", "wb") as f:
    f.write(encrypted)

