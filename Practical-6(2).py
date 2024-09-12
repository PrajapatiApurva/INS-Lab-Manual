def row_column_encrypt(plaintext, key):
    """Encrypts the plaintext using the Row-Column cipher with the given key."""
    ciphertext = ['' for _ in range(key)]
    
    for index, char in enumerate(plaintext):
        column = index % key
        ciphertext[column] += char
    
    return ''.join(ciphertext)

def row_column_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Row-Column cipher with the given key."""
    num_full_rows = len(ciphertext) // key
    extra_columns = len(ciphertext) % key

    plaintext_array = ['' for _ in range(len(ciphertext))]
    current_pos = 0

    # Fill the rows and columns according to the encryption pattern
    for col in range(key):
        for row in range(num_full_rows + 1):
            if row < num_full_rows or (row == num_full_rows and col < extra_columns):
                plaintext_array[row * key + col] = ciphertext[current_pos]
                current_pos += 1

    return ''.join(plaintext_array)

if __name__ == "__main__":
    choice = input("Choose (1) Encrypt (2) Decrypt: ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the key: "))

        if key <= 1:
            print("Error: The key must be greater than 1.")
        else:
            encrypted_message = row_column_encrypt(plaintext, key)
            print(f"Encrypted message: {encrypted_message}")

    elif choice == '2':
        ciphertext = input("Enter the ciphertext: ")
        key = int(input("Enter the key: "))

        if key <= 1:
            print("Error: The key must be greater than 1.")
        else:
            decrypted_message = row_column_decrypt(ciphertext, key)
            print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice")
