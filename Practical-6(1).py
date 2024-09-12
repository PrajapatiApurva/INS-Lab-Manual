def rail_fence_encrypt(plaintext, key):
    """Encrypts the plaintext using the Rail Fence cipher with the given key."""
    rail = ['' for _ in range(key)]
    direction = 1   
    row = 0
    for char in plaintext:
        rail[row] += char
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction
    return ''.join(rail)

def rail_fence_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Rail Fence cipher with the given key."""
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    direction = None
    row, col = 0, 0

    # Mark positions for the zigzag pattern
    for char in ciphertext:
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        rail[row][col] = '*'
        col += 1
        row += direction

    # Place ciphertext in the zigzag pattern
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the decrypted message
    result = []
    row, col = 0, 0
    for char in ciphertext:
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += direction

    return ''.join(result)

if __name__ == "__main__":
    choice = input("Choose (1) Encrypt (2) Decrypt: ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the key: "))

        if key <= 1:
            print("Error: The key must be greater than 1.")
        else:
            encrypted_message = rail_fence_encrypt(plaintext, key)
            print(f"Encrypted message: {encrypted_message}")

    elif choice == '2':
        ciphertext = input("Enter the ciphertext: ")
        key = int(input("Enter the key: "))

        if key <= 1:
            print("Error: The key must be greater than 1.")
        else:
            decrypted_message = rail_fence_decrypt(ciphertext, key)
            print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice")
