import datetime as dt
import time
from zoneinfo import ZoneInfo as zi

cali_tz = zi("America/Los_Angeles")
cali_time = dt.datetime.now(cali_tz)

print("this is running on California Time:", cali_time.strftime("%Y-%m-%d %I:%M:%S %p %Z"))
print('Welcome to your birthday countdown')

while True:
    year = int(input('Which year were you born in?\n'))
    month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))
    day = int(input('Which day in that month?\n'))
    
    try:
        date_birth = dt.datetime(year, month, day, tzinfo=cali_tz)
    except ValueError:
        print("That date calendar combination doesn't exist. Check your leap year day! Please try again.\n")
        continue

    current_time = dt.datetime.now(cali_tz)

    if date_birth > current_time:
        print("Error: You entered a future birth date! Please try again.\n")
    elif current_time.year - year > 120:
        print("Error: That birth date is too far in the past! Please try again.\n")
    else:
        break

age = current_time.year - year
if (current_time.month, current_time.day) < (month, day):
    age -= 1

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_num = date_birth.weekday()
print('You are', age, 'years old and may have forgotten which day of the week it was ...')
print('But I can tell you ... it was a ...', end = ' ')
print(weekday_names[weekday_num])

thisyear = current_time.year

try:
    thisyear_bday = dt.datetime(thisyear, month, day, tzinfo=cali_tz)
except ValueError:
    thisyear_bday = dt.datetime(thisyear, 3, 1, tzinfo=cali_tz)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    try:
        next_bday = dt.datetime(thisyear+1, month, day, tzinfo=cali_tz)
    except ValueError:
        next_bday = dt.datetime(thisyear+1, 3, 1, tzinfo=cali_tz)
    
print('Your next birthday will be on ...', end = ' ')
print(next_bday.strftime("%Y-%m-%d"))
print()
print('That will be a ...', end = ' ')
weekday_num = next_bday.weekday()
print(weekday_names[weekday_num])

print()
print()

while next_bday > current_time:
    current_time = dt.datetime.now(cali_tz)
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    total_mins_left, seconds_left  = divmod(total_seconds_left, 60)
    hrs_left, minutes_left  = divmod(total_mins_left, 60)

    print('Your next birthday is', days_left, 'days', hrs_left, 'hrs', minutes_left, 'mins', seconds_left, 'secs away.      ', end = '\r')

    time.sleep(1)

print("\n" + "=" * 50)
print(" 🎉 🎂  HAPPY BIRTHDAY! IT IS FINALLY HERE!  🎂 🎉 ")
print("=" * 50)
