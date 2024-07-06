# Subject : INS(Information and Network Security)
# Practical-1 (ceasor cipher encryption and decryption) 

def encrypt(text, shift):
  result = ""

  for i in range(len(text)):
    char = text[i]
    # Encryption of uppercase characters
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    # Encryption of lowercase characters
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char

  return result

def decrypt(text, shift):
  result = ""
 
  for i in range(len(text)):
    char = text[i]
    # Decryption of uppercase characters
    if char.isupper():
      result += chr((ord(char) - shift - 65) % 26 + 65)
    # Decryption of lowercase characters
    elif char.islower():
      result += chr((ord(char) - shift - 97) % 26 + 97)
    else:
      result += char

  return result

if __name__ == "__main__":
  text = "Apurva Girishkumar Prajapati"
  shift = 7

  encrypted_text = encrypt(text, shift)
  decrypted_text = decrypt(encrypted_text, shift)

  print(f"Original Text: {text}")
  print(f"Encrypted Text: {encrypted_text}")
  print(f"Decrypted Text: {decrypted_text}")