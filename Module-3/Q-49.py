# Write a Python function to calculate the factorial of a number (a non-negative integer).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a non-negative integer : "))
print("Factorial:", factorial(num))


