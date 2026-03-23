def list_to_unique_tuple(input_list):
    # Using dict.fromkeys() to remove duplicates while maintaining order
    unique_elements = list(dict.fromkeys(input_list))
    return tuple(unique_elements)

# Test
print("Q5:", list_to_unique_tuple([1, 2, 2, 3, 4, 4]))