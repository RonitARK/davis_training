def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)

# Test
print("Q1:", find_duplicates([1, 2, 3, 2, 4, 5, 1]))