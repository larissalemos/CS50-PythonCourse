'''
This is a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call
(e.g., one function per requirement).
Requirements:

- “All vanity plates must start with at least two letters.”
- “vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start_two_letters(s) and number_end(s):
        return True

#All vanity plates must start with at least two letters.
def start_two_letters(i):
    if i[0:2].isalpha() and 1 < len(i) < 7 and i.isalnum():
        return True

def number_end(t):
    for char in t:
        if char.isdigit():
            index = t.index(char)
            if t[index:].isdigit() and char != "0":
                return True
            else:
                return False
    else:
        return True

main()