
# Task: Display last N lines of a file

"""
1. Ask for or define N (number of lines).
2. Read all lines from the file into a list.
3. Use list slicing [-N:] to get only the last N elements
"""

n = int(input("Enter number of lines to show: "))
with open('logs.txt', 'r') as f:
    lines = f.readlines()
    # Get only the last n elements from the list
    last_n = lines[-n:] 
    for line in last_n:
        print(line.strip())
