def find_max_min_tuple(input_tuple):   
    # Initialize max and min with the first element
    maximum = input_tuple[0]
    minimum = input_tuple[0]
    
    # Iterate to find max and min without built-in functions
    for item in input_tuple[1:]:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item
            
    return f"Max = {maximum}, Min = {minimum}"

# Test
print("Q6:", find_max_min_tuple((5, 1, 8, 3)))