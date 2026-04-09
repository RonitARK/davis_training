
l = list((input("Enter numbers (comma separated): ")).split(","))
# Take the last element and add it to the beginning
rotated = [l[-1]] + l[:-1]
print(rotated)