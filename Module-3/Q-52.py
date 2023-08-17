# Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(string):
    return string == string[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a palindrome")

