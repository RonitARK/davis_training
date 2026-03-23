def set_operations(set1, set2):  
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    
    return f"Intersection: {intersection}\nDifference: {difference}"

# Test
print("Q7:\n" + set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))