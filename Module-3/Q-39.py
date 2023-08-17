# Write a Python program to check multiple keys exists in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b', 'x']
key_check = all(key in my_dict for key in keys_to_check)

if key_check:
    print("All keys exist in dictionary")
else:
    print("Not all keys exist in dictionary")
