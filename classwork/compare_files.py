
# Task: Find lines in file1 but not in file2

"""
1. Read lines from file2.txt into a set (for fast searching).
2. Read file1.txt line by line.
3. If a line from file1 is not in the file2 set, print/save it.  
"""

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    # Convert file2 to a set for comparison
    f2_content = set(f2.readlines())
    for line in f1:
        [span_34](start_span)if line not in f2_content: # Find unique lines
            print(f"Unique to File 1: {line.strip()}")
