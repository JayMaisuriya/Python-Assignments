# Write a Python program to check if a number is positive, negative or zero.
number = float(input("Enter a number: "))
if number > 0:
    print(str(number) + " is Positive")
elif number < 0:
    print(str(number) + " is Negative")
else:
    print(str(number) + " is Zero")
