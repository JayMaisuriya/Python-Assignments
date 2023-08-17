# Write a Python function to reverses a string if its length is a multiple of 4.

str_to_reverse = input("Enter a string : ")
if len(str_to_reverse) % 4 == 0:
    reversed_str = str_to_reverse[::-1]
    print("Reversed string  :", reversed_str)
else:
    print("String length is not a multiple of 4 ")

