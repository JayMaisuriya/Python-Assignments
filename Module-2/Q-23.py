# Write a Python function to insert a string in the middle of a string.

main_str = input("Enter the main string : ")
insert_str = input("Enter the string to insert : ")

middle_index = len(main_str) // 2
result = main_str[:middle_index] + insert_str + main_str[middle_index:]

print("Modified string : ", result)
