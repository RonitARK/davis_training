def check_palindrome():
    # Check if a number/string is palindrome
    original = input("Enter a string or number: ")
    
    # Use loop (while or for) to reverse the input
    reversed_str = ""
    for char in original:
        reversed_str = char + reversed_str
        
    # Use if-else to print result
    if original.lower() == reversed_str.lower():
        print("It is a palindrome.")
    else:
        print("It is NOT a palindrome.")

check_palindrome()