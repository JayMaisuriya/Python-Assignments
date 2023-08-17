# How will you create a dictionary using tuples in python?

keys = ('a', 'b', 'c')
values = (1, 2, 3)
created_dict = {}

for i in range(len(keys)):
    created_dict[keys[i]] = values[i]

print("Created dictionary:", created_dict)

