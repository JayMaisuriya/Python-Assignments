# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

given_str = input("Enter a string : ")

if len(given_str) < 3:
    result_str = given_str
elif given_str.endswith("ing"):
    result_str = given_str + "ly"
else:
    result_str = given_str + "ing"

print("Modified string :", result_str)
