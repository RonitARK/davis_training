def symmetric_diff(set1, set2):   
    # Returns elements in either set, but not both
    return set1.symmetric_difference(set2)

# Test
print("Q14:", symmetric_diff({1, 2, 3}, {3, 4, 5}))