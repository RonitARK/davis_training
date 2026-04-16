
# Task: Create a new file with unique lines only

1. Create an empty set to track "seen" lines.
2. Open the source file and a new file.
3. Only write a line to the new file if it is not in the "seen" set.  

seen_lines = set() # Set to store unique records
with open('logs.txt', 'r') as infile, open('clean_logs.txt', 'w') as outfile:
    for line in infile:
        if line not in seen_lines:
            outfile.write(line) # Save if unique
            seen_lines.add(line) # Mark as seen
