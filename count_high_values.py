

nums = list((input("Enter numbers (comma separated): ")).split(","))
nums = [int(x) for x in nums]

count = 0
for x in nums:
    if x > 50:
        count += 1
print(count)