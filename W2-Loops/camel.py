'''
This is a program that prompts the user for the name of a variable in camel case and outputs the corresponding
name in snake case. Assume that the user’s input will indeed be in camel case.
'''

camel = input("Insert the name of the variable in camelCase: ")

#Separate all letters making a list.
lst = []
for letter in camel:
    lst.append(letter)

#Test if there is any letter in uppercase and, if there is, replace it by underscore + the letter in lowercase.
for i in range(len(lst)):
    if lst[i].isupper():
        lst[i] = lst[i].replace(lst[i], "_" + lst[i].lower())

#print the name of the field in snake_case format.
snake_case = print("".join(lst))