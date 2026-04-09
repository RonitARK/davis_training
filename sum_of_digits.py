
n = int(input("Enter a number: "))
# Convert digits to a list of integers and sum them
total = sum(int(digit) for digit in str(n))
print(total)