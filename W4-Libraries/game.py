'''
This is a program that prompts the user for a level, n.
- If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
- If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
- If the guess is larger than that integer, the program should output Too large! and prompt the user again.
- If the guess is the same as that integer, the program should output Just right! and exit.
'''
import random

while True:
    try:
        n = int(input("Level: "))
        d = random.randint(0,n)
        break
    except (ValueError, NameError):
        pass
while True:
    try:
        guess = int(input("Guess: "))
        if guess > n:
            pass
        elif guess > d:
            print("Too large!")
            continue
        elif guess < d:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break
    except (ValueError, NameError):
        pass