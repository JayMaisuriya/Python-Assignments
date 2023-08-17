# Write a Python program to get a single string from two given strings separated by a space and swap the first two characters of each string.


str1 = input("\nEnter first string : ")
str2 = input("Enter second string : ")

if len(str1) >= 2 and len(str2) >= 2:
    new_str = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    print("\nSwapped string :", new_str)
else:
    print("\nStrings are too short for swapping.")
