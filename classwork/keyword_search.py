
# Task: Find lines containing a keyword

"""
1. Ask the user for a search string.
2. Open the file and iterate through each line.
3. If the keyword exists in the line, print it.
"""


keyword = input("Enter the keyword to search: ")
with open('data.txt', 'r') as f:
    for line in f:
        [span_25](start_span)if keyword in line: # Check for keyword existence
            print(line.strip())
