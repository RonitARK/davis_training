def login_system():
    # Username = "admin", Password = "1234"
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0
    
    # Allow max 3 attempts using a while loop
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Use if-else for validation
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            attempts += 1
            print(f"Incorrect. Attempts remaining: {3 - attempts}")
            
    # "Account Locked" after 3 failures [cite: 34]
    print("Account Locked")

login_system()