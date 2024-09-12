def vernam_encrypt(plaintext, key):
    """Encrypts the plaintext using the Vernam cipher with the given key."""
    ciphertext = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        ciphertext[i] = plaintext[i] ^ key[i]
    return ciphertext

def vernam_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Vernam cipher with the given key."""
    plaintext = bytearray(len(ciphertext))
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ key[i]
    return plaintext

if __name__ == "__main__":
    text = input("Enter text: ").encode()
    key_input = input("Enter key: ").encode()

    if len(key_input) < len(text):
        key = (key_input * (len(text) // len(key_input))) + key_input[:len(text) % len(key_input)]
    else:
        key = key_input[:len(text)]

    print(f"Key (hex): {key.hex()}")

    choice = input("Choose (1) Encrypt (2) Decrypt: ")

    if choice == '1':
        ciphertext = vernam_encrypt(text, key)
        print(f"Ciphertext (hex): {ciphertext.hex()}")
    elif choice == '2':
        ciphertext = bytes.fromhex(input("Enter ciphertext (in hex): "))
        if len(key) < len(ciphertext):
            key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
        plaintext = vernam_decrypt(ciphertext, key)
        print(f"Plaintext: {plaintext.decode()}")
    else:
        print("Invalid choice")
