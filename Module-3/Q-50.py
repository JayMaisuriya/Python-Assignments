# Write a Python function to check whether a number is in a given range.

def check_in_range(number, start, end):
    return start <= number <= end

num = int(input("Enter a number: "))
start_range = 10
end_range = 50
if check_in_range(num, start_range, end_range):
    print("Number is in range")
else:
    print("Number is not in range")
