# Write a Python program to returns sum of all divisors of a number.

def sum_of_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(divisors)

num = int(input("Enter a number: "))
divisor_sum = sum_of_divisors(num)
print("Sum of divisors:", divisor_sum)
