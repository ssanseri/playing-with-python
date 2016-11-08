##Scenario: The company you work for just opened two new branches. One is in New York City,
##the other in London. They need a very simple program to find out if the branches are open or
##closed based on the current time of the Headquarters here in Portland. The hours of both
##branches are 9:00AM - 9:00PM in their own time zone.
##What is asked of you:
##Create code that will use the current time of the Portland HQ to find out the time in the NYC &
##London branches, then compare that time with the branches hours to see if they are open or
##closed.
##Print out if each of the two branches are open or closed.

import datetime
from pytz import timezone
import time

def get_hms_from_datetime (my_datetime):
    hms_datetime = my_datetime.strftime(fmt)
    hms = hms_datetime.split(':')
    return hms

def business_hours (my_datetime):
    hms = get_hms_from_datetime (my_datetime)
    hrs = int(hms[0])
    mins = int(hms[1])
    secs = int(hms[2])
    if hrs < 9:
        return False
    elif hrs > 21:
        return False
    elif hrs == 21 and (mins > 0 or secs > 0):
        return False
    else:
        return True

def show_is_business_hours (my_datetime, city):
    if business_hours(my_datetime):
        print("Yes, " + city + " branch is open!")
    else:
        print("No, " + city + "branch is closed!")

#fmt = "%Y-%m-%d %H:%M%:%S %Z%z"
#fmt = "%Y-%m-%d %H:%M%:%S"
fmt = "%H:%M:%S"

# Current time in UTC
now_utc = datetime.datetime.now(timezone('UTC'))

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
print(now_pacific.strftime(fmt))
show_is_business_hours(now_pacific, "Portland")

# Convert to US/Eastern time zone
now_eastern = now_utc.astimezone(timezone('US/Eastern'))
print(now_eastern.strftime(fmt))
show_is_business_hours(now_eastern, "New York")

# Convert to London time zone
now_london = now_pacific.astimezone(timezone('Europe/London'))
print(now_london.strftime(fmt))
show_is_business_hours(now_london, "London")

