
s = input("Enter a sentence: ")
words = s.split() # Splits sentence into a list of words
# max() with key=len finds the item with the most characters
print(max(words, key=len))