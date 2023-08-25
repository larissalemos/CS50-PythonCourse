'''
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
Wouldn’t it be nice if you had a program that could tell you what to eat when?

This is a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all.
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive.
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
'''

def main():
    intime = input("What time is it? ")
    time = convert(intime)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    return float(hours) + minutes

if __name__ == "__main__":
    main()