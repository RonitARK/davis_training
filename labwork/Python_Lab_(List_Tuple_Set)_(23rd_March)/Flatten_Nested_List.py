def flatten_list(nested_list):   
    # List comprehension to iterate through sublists
    return [item for sublist in nested_list for item in sublist]

# Test
print("Q13:", flatten_list([[1, 2], [3, 4], [5]]))