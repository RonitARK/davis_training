
s = input("Enter a string: ")
dupes = []
for char in s:
    # If char appears more than once and isn't in our list yet
    if s.count(char) > 1 and char not in dupes:
        dupes.append(char)
print(" ".join(dupes))