# Write a Python program to create a dictionary from a string.

input_string = 'jay'
char_count = {}
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

print("Dictionary:", char_count)

