def generate_keys(p, q):
    """Generate public and private keys based on prime numbers p and q."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choosing e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Common choice for e
    d = pow(e, -1, phi)  # Compute d using modular inverse

    return (e, n), (d, n)

def encrypt(public_key, message):
    """Encrypts the message using the public key."""
    e, n = public_key
    return [pow(ord(char) - ord('A'), e, n) for char in message]

def decrypt(private_key, ciphertext):
    """Decrypts the ciphertext using the private key."""
    d, n = private_key
    return ''.join([chr(pow(char, d, n) + ord('A')) for char in ciphertext])

# Input section
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
message = input("Enter message in uppercase letters (A-Z): ").upper()

public_key, private_key = generate_keys(p, q)

ciphertext = encrypt(public_key, message)
print("Encrypted message:", ciphertext)

decrypted = decrypt(private_key, ciphertext)
print("Decrypted message:", decrypted)
