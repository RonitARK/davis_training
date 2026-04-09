
l1, l2 = input("Enter the first list (comma separated): ").split(","), input("Enter the second list (comma separated): ").split(",")
# Intersection (&) finds items present in both sets
common = list(set(l1) & set(l2))
print(common)