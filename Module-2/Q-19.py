# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.

input_str = input("Enter a string : ")

not_index = input_str.find("not")
poor_index = input_str.find("poor")

if not_index != -1 and poor_index != -1 and poor_index > not_index:
    modified_str = input_str[:not_index] + "good" + input_str[poor_index+4:]
    print("Modified string :", modified_str)
else:
    print("No modification needed.")
