
# Task: Basic Caesar Cipher encryption

"""
1. Define a shift value (key).
2. Read the file character by character.
3. Shift the character's Unicode value using ord() and chr().
4. Save the new characters to an output file.
"""

shift = 4
with open('message.txt', 'r') as f, open('encrypted.txt', 'w') as out:
    for char in f.read():
        # Shift the character code
        encrypted_char = chr(ord(char) + shift)
        out.write(encrypted_char)
