'''
This is a program that prompts the user for items, one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
'''
shopping_list = {}

while True:
    try:
        item = input("").upper()
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1
    except EOFError:
        print("")
        for key in sorted(shopping_list.keys()):
            print(shopping_list[key], key)
        break