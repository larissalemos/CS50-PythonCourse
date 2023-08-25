'''
This is a program that prompts the user for a date, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user
again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").title().strip()
    if "/" in date:
         month, day, year = date.split("/")
    elif "," in date:
         date = date.replace(",", "")
         month, day, year = date.split(" ")
         if month in month_list:
              month = month_list.index(month) + 1
    else:
         continue
    try:
        if int(month) > 12 or int(day)>31:
             continue
        else:
            break
    except ValueError:
            continue

print(f"{year}-{int(month):02}-{int(day):02}")