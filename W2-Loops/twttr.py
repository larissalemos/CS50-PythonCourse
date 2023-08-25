'''
This is a program that prompts the user for a str of text and then outputs that same text but with all vowels
(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

s = input("Input: ")
Output = print("Output: ", end="")
#Test if there is any vowels and delete them.

for letter in s:
    if not letter in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        print(letter, end ="")
print()