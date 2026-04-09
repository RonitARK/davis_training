
nums = list((input("Enter numbers (comma separated): ")).split(","))
max_val = nums[0] # Assume the first number is the biggest
for n in nums:
    if n > max_val:
        max_val = n # Update max_val if a bigger number is found
print(max_val)