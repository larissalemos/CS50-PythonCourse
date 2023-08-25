'''
This is a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins,n, that they would like to buy.
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
among whose nested keys is the current price of Bitcoin as a float.
- Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.
'''

import sys
import json
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif not sys.argv[1].replace('.', '', 1).isdigit():
        sys.exit("Command-line argument is not a number")
    else:
        source = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if source.status_code == 200:
            sourcej = source.json()
            price = sourcej["bpi"]["USD"]["rate_float"]
            amount = float(sys.argv[1]) * price
            print(f"${amount:,.4f}")
        else:
            sys.exit("")

except requests.RequestException:
    sys.exit("")