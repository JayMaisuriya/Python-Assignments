# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2,return instead of the empty string.

sample_str = input("Enter a string : ")

if len(sample_str) < 2:
    print("Empty String")
else:
    modified_str = sample_str[:2] + sample_str[-2:]
    print("Modified string :", modified_str)

    