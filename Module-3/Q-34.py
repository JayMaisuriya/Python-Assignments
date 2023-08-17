# Write a Python script to concatenate following dictionaries to create a new one.

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}

dict3 = dict1.copy()
dict3.update(dict2)

print("Concatenated dictionary : ", dict3)
