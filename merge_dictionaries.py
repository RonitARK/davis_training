
def collect_dictionary(name):
    """Helper function to create a dictionary from user input."""
    data = {}
    print(f"\n--- Create Dictionary: {name} ---")
    print("Enter key-value pairs (Type 'done' to stop for this dictionary)")
    
    while True:
        key = input("Enter key: ")
        if key.lower() == 'done':
            break
        
        val = input(f"Enter integer value for '{key}': ")
        
        # Convert input to integer before storing
        try:
            data[key] = int(val)
        except ValueError:
            print("Error: Please enter a valid integer.")
            
    return data

# Collect two dictionaries from the user
d1 = collect_dictionary("First")
d2 = collect_dictionary("Second")

# Merge d2 into d1 using update() 
# Note: If a key exists in both, d2's value will overwrite d1's value.
d1.update(d2)

# Display the final result 
print("\n--- Merged Dictionary ---")
print(d1)