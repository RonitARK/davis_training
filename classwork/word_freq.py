
 #Task: Count frequency of each word in article.txt

1. Read the file and convert text to lowercase.
2. Remove punctuation characters.
3. Split text into a list of words.
4. Use a dictionary to store and increment word counts.  
  
 
counts = {}
with open('article.txt', 'r') as f:
    # Lowercase and remove basic punctuation
    text = f.read().lower().replace('.', '').replace(',', '')
    words = text.split() # Get individual words
    for word in words:
        # Update word count in dictionary
        counts[word] = counts.get(word, 0) + 1
print(counts)

