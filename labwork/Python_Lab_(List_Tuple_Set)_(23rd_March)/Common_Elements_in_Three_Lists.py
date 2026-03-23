def common_in_three_lists(list1, list2, list3):   
    # Convert to sets and find the intersection
    common_set = set(list1).intersection(set(list2), set(list3))
    return list(common_set)

# Test
print("Q12:", common_in_three_lists([1, 2, 3], [2, 3, 4], [2, 5, 3]))