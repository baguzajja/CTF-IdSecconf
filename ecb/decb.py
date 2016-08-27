from Crypto.Cipher
import AES, XOR
IV_SIZE = 16
BLOCK_SIZE = 16




block_size = AES.block_size


def decrypt(key, ciphertext):
    # assume: len(key) == 16 bytes; PKCS5 padding scheme; len(IV) == 16 bytes
    iv = ciphertext[:block_size]
    ciph = ciphertext[block_size:]
    
    assert len(ciph) % block_size == 0
    
    cipher = AES.new(key)
    plain_blocks = []
    previous_ciph_block = iv
    for i in range(len(ciph) / block_size):
        xor = XOR.new(previous_ciph_block)
        
        ciph_block = ciph[(i*block_size):((i+1)*block_size)]
        plain_block = xor.decrypt(cipher.decrypt(ciph_block))
        
        previous_ciph_block = ciph_block
        plain_blocks.append(plain_block)
    
    # remove plaintext padding
    padded_plaintext = ''.join(plain_blocks)
    num_padded_bytes = ord(padded_plaintext[-1])

return padded_plaintext[:(0-num_padded_bytes)]


if __name__ == '__main__':
    keys_ciphertexts_hex = [
                            ('140b41b22a29beb4061bda66b6747e14', '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'),
                            ('140b41b22a29beb4061bda66b6747e14', '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'),
                            ]
        
                            for key_hex, ciphertext_hex in keys_ciphertexts_hex:
                                key = key_hex.decode('hex')
                                    ciphertext = ciphertext_hex.decode('hex')
                                        
                                        print repr(decrypt(key, ciphertext))