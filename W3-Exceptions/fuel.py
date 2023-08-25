'''
This is a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though,
1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                return round((x/y)*100)
            else:
                pass
        except (ValueError, ZeroDivisionError, NameError):
            pass

def main():
    fuel = get_fraction()
    if fuel >= 99:
        print ("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")

main()