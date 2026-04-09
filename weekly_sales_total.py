
#sales = [100, 200, 150, 300, 250, 400, 100]
sales = list((input("Enter sales for 7 days (comma separated): ")).split(","))
# Convert each sales figure to an integer
sales = [int(sale) for sale in sales]
# sum() adds all numbers in the list
print(sum(sales))