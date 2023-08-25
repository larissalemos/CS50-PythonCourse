'''
This is a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and.
'''
import inflect
p = inflect.engine()

adieu_list = []

while True:
    try:
        item = input("Name: ")
    except EOFError:
        break
    adieu_list.append(item)

adieu = p.join(adieu_list)
print("Adieu, adieu, to " + adieu)