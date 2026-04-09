
s = input("Enter a string: ")
result = ""
for char in s:
    # ASCII value of 'a' is 97, 'A' is 65. Difference is 32.
    result += chr(ord(char) - 32)
print(result)