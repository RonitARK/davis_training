
# Task: Extract valid emails from data.txt

"""
1. Read the entire file content.
2. Split content into individual words.
3. Check if a word contains "@" and a "." after it.
4. Save valid emails to emails.txt.
"""

with open('data.txt', 'r') as f, open('emails.txt', 'w') as out:
    words = f.read().split()
    for word in words:
        # Simple check for email structure
        if '@' in word and '.' in word.split('@')[-1]:
            out.write(word + '\n')
