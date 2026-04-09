
def filter_evens(nums):
    return [x for x in nums if x % 2 == 0]

print(filter_evens([int(x) for x in input("Enter numbers (comma separated): ").split(",")]))