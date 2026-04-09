
dict = dict(item.split(":") for item in input("Enter key-value pairs (key:value, comma separated): ").split(","))
key = input("Enter key to check: ")
if key in dict:
    print("Yes")
else:
    print("No")