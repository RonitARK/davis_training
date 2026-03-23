def tuples_to_dict(keys_tuple, values_tuple):   
    # Use zip to pair elements and dict() to map them
    return dict(zip(keys_tuple, values_tuple))

# Test
print("Q15:", tuples_to_dict(('a', 'b', 'c'), (1, 2, 3)))