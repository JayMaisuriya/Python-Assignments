# Write a Python function to get the largest number, smallest num and sum of all from a list.

def list_stats(my_list):
    largest = max(my_list)
    smallest = min(my_list)
    total_sum = sum(my_list)
    return largest, smallest, total_sum

num_list = [10, 5, 20, 3, 15]
largest_num, smallest_num, sum_nums = list_stats(num_list)
print("Largest :", largest_num)
print("Smallest :", smallest_num)
print("Sum :", sum_nums)
