# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [
    x + y
    for x in data['1']
    for y in data['2']
]

print("Combinations:", ' '.join(combinations))

 
