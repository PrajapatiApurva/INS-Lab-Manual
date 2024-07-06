# Subject : INS(Information and Network Security)
# Practical-4 (hill cipher encryption and decryption)

def create_key_matrix(key):
    key = key.upper().replace(" ", "")
    if len(key) != 4:
        raise ValueError("Key must be 4 characters long for a 2x2 matrix.")
    key_matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(ord(key[i * 2 + j]) % 65)
        key_matrix.append(row)
    return key_matrix

def text_to_vector(text):
    vector = []
    for char in text:
        vector.append(ord(char.upper()) % 65)
    return vector

def vector_to_text(vector):
    text = ""
    for num in vector:
        text += chr(num + 65)
    return text

def matrix_mod_inv_2x2(matrix, mod):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    det_inv = pow(det, -1, mod)
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible")

    adjugate = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    inv_matrix = [[(det_inv * adjugate[0][0]) % mod, (det_inv * adjugate[0][1]) % mod],
                  [(det_inv * adjugate[1][0]) % mod, (det_inv * adjugate[1][1]) % mod]]

    return inv_matrix

def preserve_case(plaintext, transformed_text):
    result = ""
    for i, char in enumerate(plaintext):
        if char.isupper():
            result += transformed_text[i].upper()
        else:
            result += transformed_text[i].lower()
    return result

def encrypt(plaintext, key_matrix):
    original_text = plaintext
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        block = text_to_vector(plaintext[i:i + 2])
        encrypted_block = [
            (key_matrix[0][0] * block[0] + key_matrix[0][1] * block[1]) % 26,
            (key_matrix[1][0] * block[0] + key_matrix[1][1] * block[1]) % 26
        ]
        ciphertext += vector_to_text(encrypted_block)

    return preserve_case(original_text, ciphertext)

def decrypt(ciphertext, key_matrix):
    original_text = ciphertext
    ciphertext = ciphertext.upper().replace(" ", "")
    key_matrix_inv = matrix_mod_inv_2x2(key_matrix, 26)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        block = text_to_vector(ciphertext[i:i + 2])
        decrypted_block = [
            (key_matrix_inv[0][0] * block[0] + key_matrix_inv[0][1] * block[1]) % 26,
            (key_matrix_inv[1][0] * block[0] + key_matrix_inv[1][1] * block[1]) % 26
        ]
        plaintext += vector_to_text(decrypted_block)

    return preserve_case(original_text, plaintext)

if __name__ == "__main__":
    key = input("Enter 4-letter key: ")
    key_matrix = create_key_matrix(key)

    plaintext = input("Enter text: ")
    
    choice = int(input("Enter 1 to Encrypt, 2 to Decrypt: "))
    if choice == 1:
        print("Ciphertext:", encrypt(plaintext, key_matrix))
    elif choice == 2:
        print("Plaintext:", decrypt(plaintext, key_matrix))
    else:
        print("Invalid choice")
