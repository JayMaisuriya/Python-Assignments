# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a == b or b == c or c == a:
    print("Sum is 0")
else:
    print("Sum : ", a + b + c)
