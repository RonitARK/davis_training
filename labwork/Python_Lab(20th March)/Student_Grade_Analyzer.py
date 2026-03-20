def calculate_grade(marks):
	# Takes marks (0-100) and uses if-elif-else to assign grades
	if marks >= 90:
		return "A"
	elif marks >= 75:
		return "B"
	elif marks >= 50:
		return "C"
	else:
		return "Fail"

# Use a loop to process marks of 5 students
for student_number in range(1, 6):
	marks = float(input(f"Enter marks for Student {student_number} (0-100): "))

	if 0 <= marks <= 100:
		grade = calculate_grade(marks)
		print(f"Student {student_number}: {grade}")
	else:
		print(f"Student {student_number}: Invalid marks")