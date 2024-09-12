import os

def xor_bytes(a, b):
    """XORs two byte sequences."""
    return bytes([x ^ y for x, y in zip(a, b)])

def encrypt(plaintext, key):
    """Encrypts the plaintext using XOR with the given key."""
    plaintext_bytes = plaintext.encode()
    if len(key) < len(plaintext_bytes):
        raise ValueError("Key must be at least as long as the plaintext")
    ciphertext = xor_bytes(plaintext_bytes, key)
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypts the ciphertext using XOR with the given key."""
    if len(key) < len(ciphertext):
        raise ValueError("Key must be at least as long as the ciphertext")
    plaintext_bytes = xor_bytes(ciphertext, key)
    return plaintext_bytes.decode()

if __name__ == "__main__":
    choice = input("Choose (1) Encrypt (2) Decrypt: ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = input("Enter the key (must be at least as long as the plaintext): ")
        
        if len(key) < len(plaintext):
            print("Error: Key must be at least as long as the plaintext.")
        else:
            key_bytes = key.encode()
            ciphertext = encrypt(plaintext, key_bytes)
            print(f"Ciphertext (in hex): {ciphertext.hex()}")

    elif choice == '2':
        ciphertext_hex = input("Enter the ciphertext (in hex): ")
        key = input("Enter the key (must be at least as long as the ciphertext): ")
        
        ciphertext = bytes.fromhex(ciphertext_hex)
        
        if len(key) < len(ciphertext):
            print("Error: Key must be at least as long as the ciphertext.")
        else:
            key_bytes = key.encode()
            plaintext = decrypt(ciphertext, key_bytes)
            print(f"Decrypted plaintext: {plaintext}")

    else:
        print("Invalid choice")
