def merge_and_sort_unique(list1, list2):  
    # Combine, convert to set for uniqueness, back to list, then sort
    combined_unique = sorted(list(set(list1 + list2)))
    return combined_unique

# Test
print("Q9:", merge_and_sort_unique([3, 1, 2], [2, 4, 5]))