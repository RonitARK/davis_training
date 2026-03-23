def check_subset(set1, set2):  
    # Check if set1 is a subset of set2
    return set1.issubset(set2)

# Test
print("Q8:", check_subset({1, 2}, {1, 2, 3, 4}))