"""

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

"""

word=input("Enter a word: ")

print(word,",",word[::-1])

if word == word[::-1]:
    print(word + " is a palindrome!")
else:
    print(word + " is not a palindrome!")
