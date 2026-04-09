
def is_prime(n):
    if n < 2: return "Not Prime"
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(int(input("Enter a number: "))))