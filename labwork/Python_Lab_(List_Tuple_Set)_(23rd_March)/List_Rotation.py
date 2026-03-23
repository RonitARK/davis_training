def rotate_list(input_list, k):   
    # Handle cases where k is larger than the list length
    k = k % len(input_list) 
    
    # Slice the list to rotate
    return input_list[-k:] + input_list[:-k]

# Test
print("Q2:", rotate_list([10, 20, 30, 40, 50], 2))