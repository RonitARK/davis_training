
# Task: Extract students with marks > 75

"""
1. Open students.txt and a new output file.
2. Loop through each line and split by commas.
3. Convert the "marks" string to a float.
4. If marks > 75, write the line to the new file.
"""

with open('students.txt', 'r') as infile, open('high_scorers.txt', 'w') as outfile:
    for line in infile:
        # Split line into components
        name, marks, city = line.strip().split(',')
        if float(marks) > 75:  # Check condition
            outfile.write(line) # Save valid record
