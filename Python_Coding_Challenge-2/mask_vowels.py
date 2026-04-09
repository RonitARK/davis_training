
s = input("Enter a string: ")
masked = ""
for char in s:
    if char in "aeiou":
        masked += "*"
    else:
        masked += char
print(masked)