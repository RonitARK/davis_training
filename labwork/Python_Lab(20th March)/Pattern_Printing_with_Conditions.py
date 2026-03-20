def print_conditional_pattern(rows):
    # Print triangle pattern using for loop
    for i in range(1, rows + 1):
        # If row number is even print *
        if i % 2 == 0:
            print("*" * i)
        # If odd print
        else:
            print("#" * i)
            
print_conditional_pattern(4)