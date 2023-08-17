# Write a Python program to check whether a list contains a sub list.

main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]

contains_sublist = True
for item in sub_list:
    if item not in main_list:
        contains_sublist = False
        break

if contains_sublist:
    print("Main list contains sub-list")
else:
    print("Main list does not contain sub-list")
