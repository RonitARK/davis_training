
# Task: Write file content in reverse order (line-wise)

"""
1. Read all lines of the file into a list.
2. Reverse the list using slicing or the reversed() function.
3. Write the reversed list into a new file.
"""

with open('input.txt', 'r') as f:
    lines = f.readlines() # Read all lines into a list
with open('reversed.txt', 'w') as out:
    # Use [::-1] to reverse the list of lines
    out.writelines(lines[::-1])
