
year = int(input("Year: "))
# A year is leap if divisible by 4 AND not 100, OR divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")