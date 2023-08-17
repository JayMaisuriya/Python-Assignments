# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 5, 'e': 4}

sorted_asc = {}
for key in sorted(my_dict, key=my_dict.get):
    sorted_asc[key] = my_dict[key]

sorted_desc = {}
for key in sorted(my_dict, key=my_dict.get, reverse=True):
    sorted_desc[key] = my_dict[key]

print("Sorted ascending:", sorted_asc)
print("Sorted descending:", sorted_desc)
