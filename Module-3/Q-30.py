# Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 2), (3, 4), (5, 6)]
unzipped = list(zip(*list_of_tuples))
print("Unzipped lists:", unzipped)
