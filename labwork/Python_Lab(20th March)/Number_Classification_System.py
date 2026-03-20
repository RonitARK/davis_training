# Takes a list of numbers and uses a function to check
def classify_numbers(numbers_list):
    # Use a for loop to process all numbers
    for num in numbers_list:
        # Check Positive / Negative / Zero
        if num > 0:
            sign = "Positive"
        elif num < 0:
            sign = "Negative"
        else:
            sign = "Zero"
            
        # Even / Odd (nested if)
        if num != 0:
            if num % 2 == 0:
                parity = "Even"
            else:
                parity = "Odd"
            print(f"{num} is {sign} and {parity}.")
        else:
            print(f"{num} is {sign}.")

# classify_numbers([10, -5, 0, 7, -4])
numbers_list = [10, -5, 0, 7, -4]
print(classify_numbers(numbers_list))