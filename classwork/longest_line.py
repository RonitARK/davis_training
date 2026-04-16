
# Task: Identify the longest line and its length

"""
1. Initialize a variable for the longest_line as an empty string.
2. Iterate through every line in the file.
3. If the current line's length is greater than the stored longest_line, update it
"""


longest = ""
with open('article.txt', 'r') as f:
    for line in f:
        if len(line) > len(longest):
            longest = line # Update if longer line found
print(f"Longest Length: {len(longest)}")
print(f"Content: {longest.strip()}")
