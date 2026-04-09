
l = list((input("Enter numbers (comma separated): ")).split(","))
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i] # Swap elements
print(l)