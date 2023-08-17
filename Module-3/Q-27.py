# Write a Python program to replace last value of tuples in a list.

tuple_list = [(1, 2), (3, 4), (5, 6)]
new_list = []

for t in tuple_list:
    modified_tuple = t[:-1] + (10,)
    new_list.append(modified_tuple)

print("Modified list : ", new_list)

