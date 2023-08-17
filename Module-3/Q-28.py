# Write a Python program to find the repeated items of a tuple.

num = (1, 2, 3, 2, 4, 2, 4, 5)
repeated_items = []

for item in num:
    if num.count(item) > 1:
        repeated_items.append(item)

unique_repeated = list(set(repeated_items))
print("Repeated items:", unique_repeated)
