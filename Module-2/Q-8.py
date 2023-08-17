# Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter : ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The letter (",letter,") Is Vowel")
else:
    print("The letter (",letter,") Is Not Vowel")
