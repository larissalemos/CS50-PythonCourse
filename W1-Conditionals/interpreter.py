'''
This is a program that prompts the user for an arithmetic expression and then calculates and outputs the result
as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
x is an integer
y is +, -, *, or /
z is an integer
'''

print("Input an expression formatted as x y z, where x is an integer, y is an operator +, -, * or /, and z is another integer.")
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        print(f"{x + z: .1f}")
match y:
    case "-":
        print(f"{x - z: .1f}")
match y:
    case "*":
        print(f"{x * z: .1f}")
match y:
    case "/":
        print(f"{x / z: .1f}")