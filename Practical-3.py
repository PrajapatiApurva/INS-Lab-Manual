# Subject : INS(Information and Network Security)
# Practical-3 (playfair cipher encryption and decryption) 

def generate_key_square(key):
    # Generating a key square for the Playfair cipher.
    key = key.upper().replace('J', 'I')
    key_square = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char.isalpha():
            key_square.append(char)
            used_chars.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            key_square.append(char)
            used_chars.add(char)

    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_square):
    for i, row in enumerate(key_square):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    plaintext = plaintext.replace('J', 'I')
    plaintext = plaintext.replace('j', 'i') 
    
    key_square = generate_key_square(key)
    plaintext_pairs = []

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]
        else:
            char2 = 'X'

        if char1 == char2:
            plaintext_pairs.append((char1, 'X'))
            i += 1
        else:
            plaintext_pairs.append((char1, char2))
            i += 2
    print(plaintext_pairs)
    ciphertext = []
    for char1, char2 in plaintext_pairs:
        row1, col1 = find_position(char1.upper(), key_square)
        row2, col2 = find_position(char2.upper(), key_square)

        if row1 == row2:
            ciphertext.append(key_square[row1][(col1 + 1) % 5] if char1==char1.upper() else key_square[row1][(col1 + 1) % 5].lower())
            ciphertext.append(key_square[row2][(col2 + 1) % 5] if char2==char2.upper() else key_square[row2][(col2 + 1) % 5].lower())
        elif col1 == col2:
            ciphertext.append(key_square[(row1 + 1) % 5][col1] if char1==char1.upper() else key_square[(row1 + 1) % 5][col1].lower())
            ciphertext.append(key_square[(row2 + 1) % 5][col2] if char2==char2.upper() else key_square[(row2 + 1) % 5][col2].lower())
        else:
            ciphertext.append(key_square[row1][col2] if char1==char1.upper() else key_square[row1][col2].lower())
            ciphertext.append(key_square[row2][col1] if char2==char2.upper() else key_square[row2][col1].lower())

    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    ciphertext_pairs = []

    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        ciphertext_pairs.append((char1, char2))
        i += 2

    plaintext = []
    for char1, char2 in ciphertext_pairs:
        row1, col1 = find_position(char1.upper(), key_square)
        row2, col2 = find_position(char2.upper(), key_square)

        if row1 == row2:
            plaintext.append(key_square[row1][(col1 - 1) % 5] if char1.isupper() else key_square[row1][(col1 - 1) % 5].lower())
            plaintext.append(key_square[row2][(col2 - 1) % 5] if char2.isupper() else key_square[row2][(col2 - 1) % 5].lower())
        elif col1 == col2:
            plaintext.append(key_square[(row1 - 1) % 5][col1] if char1.isupper() else key_square[(row1 - 1) % 5][col1].lower())
            plaintext.append(key_square[(row2 - 1) % 5][col2] if char2.isupper() else key_square[(row2 - 1) % 5][col2].lower())
        else:
            plaintext.append(key_square[row1][col2] if char1.isupper() else key_square[row1][col2].lower())
            plaintext.append(key_square[row2][col1] if char2.isupper() else key_square[row2][col1].lower())

    return ''.join(plaintext).replace('X', '')

def printKeySquare(key_square):
    for row in key_square:
        print('[', end=" ")
        for col in row:
            print(col, end=" ")
        print("]",end=" ")
        print()

if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the Word: ")
    plaintext = plaintext.replace(" ", "")  # Remove spaces

    key_square = generate_key_square(key)
    
    choice = int(input("Enter 1 for encryption and 2 for decryption: "))
    if choice == 1:
        printKeySquare(key_square)
        encrypted_text = playfair_encrypt(plaintext, key)
        print(f"Original text: {plaintext}")
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 2:
        printKeySquare(key_square)
        decrypted_text = playfair_decrypt(plaintext, key)
        print(f"Original text: {plaintext}")
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice. Please enter 1 or 2.")