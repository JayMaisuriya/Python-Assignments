# Write a Python function to check whether a number is perfect or not.

def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

num = int(input("Enter a number: "))
if is_perfect(num):
    print("Perfect number")
else:
    print("Not a perfect number")


