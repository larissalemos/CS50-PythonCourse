'''
This is a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100.
Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''
greeting = input("How would you like to greet me today? ").strip().casefold()
match greeting:
    case str() as g if g.startswith("hello"):
        print("$0")
    case str() as s if s.startswith("h"):
        print("$20")
    case _:
        print("$100")