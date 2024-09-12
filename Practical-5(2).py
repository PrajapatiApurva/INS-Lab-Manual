def vigenere_encrypt(plaintext, key):
    """Encrypts the plaintext using the Vigenère cipher with the given key."""
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    ciphertext = ""
    for i in range(len(plaintext)):
        p = ord(plaintext[i].upper())
        k = ord(key[i].upper())
        c = chr(((p + k - 2 * ord('A')) % 26) + ord('A'))
        ciphertext += c
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Vigenère cipher with the given key."""
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    plaintext = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        k = ord(key[i].upper())
        p = chr(((c - k + 26) % 26) + ord('A'))
        plaintext += p
    return plaintext

if __name__ == "__main__":
    text = input("Enter text: ").upper()
    key = input("Enter key: ").upper()

    if len(key) < len(text):
        key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    else:
        key = key[:len(text)]

    choice = input("Choose (1) Encrypt (2) Decrypt: ")

    if choice == '1':
        ciphertext = vigenere_encrypt(text, key)
        print(f"Ciphertext: {ciphertext}")
    elif choice == '2':
        ciphertext = text
        plaintext = vigenere_decrypt(ciphertext, key)
        print(f"Plaintext: {plaintext}")
    else:
        print("Invalid choice")
