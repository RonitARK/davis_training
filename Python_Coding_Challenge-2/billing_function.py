
def calculate_bill(prices):
    return sum(prices)

print(calculate_bill([int(x) for x in input("Enter prices (comma separated): ").split(",")]))