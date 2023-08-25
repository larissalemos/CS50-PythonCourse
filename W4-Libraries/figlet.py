'''
This is a program that: Expects zero or two command-line arguments:
- Zero if the user would like to output text in a random font.
- Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
the program should exit via sys.exit with an error message.
'''

import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

fonts_list = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts_list))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts_list:
    figlet.setFont(font = sys.argv[2])

else:
    sys.exit("Invalid input")

text = input("Input: ")
print(f"Output: {figlet.renderText(text)}")