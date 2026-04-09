
nums = [int(x) for x in input("Enter numbers (comma separated): ").split(",")]
freq = {}
for n in nums:
    # Get current count (default 0) and add 1
    freq[n] = freq.get(n, 0) + 1
print(freq)