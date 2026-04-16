
# Task: Merge two files with line numbers

"""
1. Read all lines from file1.txt and file2.txt.
2. Combine the lists of lines.
3. Use a loop with enumerate to add line numbers starting from 1
"""

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('merged.txt', 'w') as out:
    all_lines = f1.readlines() + f2.readlines() # Combine both files
    for i, line in enumerate(all_lines, 1): # Start counting at 1
        out.write(f"{i}: {line}")
