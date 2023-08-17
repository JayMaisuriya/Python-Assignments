# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

squares = []
for x in range(1, 31):
    squares.append(x ** 2)

subset = squares[:5] + squares[-5:]

print("First and last square numbers : ", subset)

