# Subject : INS(Information and Network Security)
# Practical-2 (monoalphabetic cipher encryption and decryption) 
import string
import random

def generate_cipher_key():
    # Generating a random monoalphabetic cipher key.
    letters_lower = list(string.ascii_lowercase)
    shuffled_letters_lower = letters_lower[:]
    random.shuffle(shuffled_letters_lower)
    
    letters_upper = list(string.ascii_uppercase)
    shuffled_letters_upper = letters_upper[:]
    random.shuffle(shuffled_letters_upper)
    
    lower=dict(zip(letters_lower, shuffled_letters_lower))
    upper=dict(zip(letters_upper, shuffled_letters_upper))
    
    finalDict = {**lower, **upper}
    
    return finalDict

def encode(plaintext, cipher_key):
    # Encoding a plaintext using the provided cipher key.
    encoded_text = ''
    for char in plaintext:
        if char in cipher_key:
            encoded_text += cipher_key[char]
        else:
            encoded_text += char
    return encoded_text

def decode(ciphertext, cipher_key):
    # Decoding a ciphertext using the provided cipher key.
    reversed_key = {v: k for k, v in cipher_key.items()}
    decoded_text = ''
    for char in ciphertext:
        if char in reversed_key:
            decoded_text+=reversed_key[char]
        else:
            decoded_text+=char
    return decoded_text

if __name__ == "__main__":
    cipher_key = generate_cipher_key()
    
    for key, value in cipher_key.items():
        print('{',key, ':', value,'}',end=',',sep='')
    print('\n')
    plaintext = "Apurva girishkumar prajapati"
    ciphertext = encode(plaintext, cipher_key)
    decoded_text = decode(ciphertext, cipher_key)

    print("Plaintext   :", plaintext)
    print("Ciphertext  :", ciphertext)
    print("Decoded Text:", decoded_text)