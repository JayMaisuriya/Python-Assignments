# Write a Python program to find the highest 3 values in a dictionary.

my_dict = {'a': 5, 'b': 10, 'c': 2, 'd': 20, 'e': 8}
highest_3 = sorted(my_dict.values(), reverse=True)[:3]
print("Highest 3 values:", highest_3)


