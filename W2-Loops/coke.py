'''
This is a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''


due = 50
while due > 0:
    coin = int(input("Insert coin: "))
    if coin != 5 and coin !=10 and coin != 25:
        print(f"Amount Due: {due}")
    else:
        due = due - coin
        if due > 0:
            print(f"Amount Due: {due}")
        else:
            print(f"Change Owed: {abs(due)}")