
d = {}
print("Enter key-value pairs (Type 'done' to finish)")

while True:
    key = input("Enter key (name/label): ")
    if key.lower() == 'done':
        break
        
    val = input(f"Enter integer value for '{key}': ")
    
    # Convert the input value to an integer and add to dictionary
    try:
        d[key] = int(val)
    except ValueError:
        print("Invalid input! Please enter a whole number for the value.")

# sorted(d.items()) returns a list of tuples sorted by the key 
sorted_items = sorted(d.items())

# Convert the sorted list back into a dictionary 
sorted_dict = dict(sorted_items)

print("\nSorted Dictionary:")
print(sorted_dict)