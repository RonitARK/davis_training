def tuple_pair_sum(input_tuple, target_sum):   
    pairs = []
    n = len(input_tuple)
    
    # Iterate through combinations
    for i in range(n):
        for j in range(i + 1, n):
            if input_tuple[i] + input_tuple[j] == target_sum:
                pairs.append((input_tuple[i], input_tuple[j]))
                
    return pairs

# Test
print("Q10:", tuple_pair_sum((1, 2, 3, 4, 5), 5))