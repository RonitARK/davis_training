
# Task: Copy contents from one file to another

"""
1. Open the source file in read mode.
2. Open the destination file in write mode.
3. Read all data from the source and write it into the destination.
4. Close both files (handled automatically by with).
"""

try:
    # Open source for reading ('r') and destination for writing ('w')
    with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
        content = src.read()  # Read entire content
        dest.write(content)   # Write content to new file
    print("File copied successfully.")
except FileNotFoundError:
    print("The source file was not found.")
