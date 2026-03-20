# Write a function is_prime(n)
def is_prime(n):  
    # Use for loop to check divisibility
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False # Return True/False
    return True

def run_prime_checker():
    try:
        num = int(input("Enter a number to check: "))
        # Use if-else to display result
        if is_prime(num):
            print(f"{num} is a Prime number.")
        else:
            print(f"{num} is NOT a Prime number.")
    except ValueError:
        print("Please enter a valid integer.")

run_prime_checker()