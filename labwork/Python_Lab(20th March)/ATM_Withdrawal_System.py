def atm_withdrawal():
    # Initial balance = 10000
    balance = 10000.0
    
    # Use while loop until user exits
    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        # Ask withdrawal amount
        user_input = input("Enter withdrawal amount (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        amount = float(user_input)
        # Conditions
        if amount < 0:
            print("Error: Invalid amount (<0)")
        elif amount > balance:
            print("Error: Insufficient balance")
        else:
            balance -= amount
            print(f"Successful withdrawal of ${amount:.2f}")

atm_withdrawal()