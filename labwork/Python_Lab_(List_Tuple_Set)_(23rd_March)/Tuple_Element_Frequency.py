def tuple_frequency(input_tuple):   
    frequency_dict = {}
    for item in input_tuple:
        # Increment count if item exists, else default to 0 and add 1
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
        
    return frequency_dict

# Test
print("Q4:", tuple_frequency((1, 2, 2, 3, 1, 4)))