def remove_empty_sets(input_list):    
    # Keep items that evaluate to True (non-empty sets)
    return [s for s in input_list if s]

# Test
print("Q11:", remove_empty_sets([{1, 2}, set(), {3, 4}, set()]))