# Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple_list = [(1, 2), (), (3, 4), (), (5, 6), ()]
non_empty_tuples = []

for t in tuple_list:
    if t:
        non_empty_tuples.append(t)

print("List with non-empty tuples:", non_empty_tuples)


