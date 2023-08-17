# Write a Python program to map two lists into a dictionary.



keys = ['a', 'b', 'c']
values = [1, 2, 3]
created_dict = {}

for i in range(len(keys)):
    created_dict[keys[i]] = values[i]

print("Mapped dictionary:", created_dict)
