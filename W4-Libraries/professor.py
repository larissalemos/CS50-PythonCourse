'''
implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
'''

import random


def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                break
        except (ValueError, NameError):
            pass
    return level

def generate_integer(level):
    score = 0

    for problems in range(10):
        trials = 3
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        else:
            raise ValueError

        while trials > 0:
            result = str(x + y)
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer == result:
                score += 1
                break
            elif answer != result and trials > 1:
                print("EEE")
                trials -= 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {result}")
                break
    print(score)


if __name__ == "__main__":
    main()