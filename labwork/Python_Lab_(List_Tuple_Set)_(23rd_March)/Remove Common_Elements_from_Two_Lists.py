def remove_common_elements(list1, list2):  
    set2 = set(list2)
    return [item for item in list1 if item not in set2]

# Test
print("Q3:", remove_common_elements([1, 2, 3, 4], [3, 4, 5]))