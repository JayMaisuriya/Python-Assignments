# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word_length(word_list):
    return max(len(word) for word in word_list)

word_list = input("Enter a list of words (comma-separated): ").split(",")
print("Length of the longest word  :", longest_word_length(word_list))
