
marks = dict(item.split(":") for item in input("Enter student names and marks (name:mark, comma separated): ").split(","))
# Get the key associated with the maximum value
top_student = max(marks, key=marks.get)
print(top_student)