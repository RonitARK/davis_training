def generate_table():
    # Takes a number from user
    num = int(input("Enter a number for the multiplication table: "))
        
    # Use if to restrict negative input
    if num < 0:
        print("Error: Negative input is not allowed.")
    else:
        # Uses for loop to print table (1-10)
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
            
generate_table()