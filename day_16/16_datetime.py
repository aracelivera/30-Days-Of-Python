##  Day 16 - 30DaysOfPython Challenge

##  Date Time

import datetime
print(dir(datetime)) # with dir is possible to know the available functions in a certain module
#['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

#   Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2023-05-26 17:43:28.130011
day = now.day                   # 26
month = now.month               # 5
year = now.year                 # 2023
hour = now.hour                 # 17
minute = now.minute             # 43
second = now.second
timestamp = now.timestamp() # Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
print(day, month, year, hour, minute) # 26 5 2023 17 43
print('timestamp', timestamp) # timestamp 1685133808.130011
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 26/5/2023, 17:43

#   Formatting Date Output Using strftime
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

#   Formatting date time using strftime method: https://strftime.org/
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t) # time: 17:49:48
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one) # time one: 05/26/2023, 17:49:48
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two) # time two: 26/05/2023, 17:49:48

#   String to Time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string) # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) # date_object = 2019-12-05 00:00:00

#   Using date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2023-05-26
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2023
print("Current month:", today.month) # 5
print("Current day:", today.day)     # 25

#   Time Objects to Represent Time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a) # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b) # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c) # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555) # d = 10:30:50.200555
print("d =", d)

#   Difference Between Two Points in Time Using
from datetime import date, datetime
today = date(year=2023, month=5, day=26)
new_year = date(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  220 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2023, month = 5, day = 26, hour = 18, minute = 51, second = 0)
t2 = datetime(year = 2024, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 219 days, 5:09:00

# Difference Between Two Points in Time Using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20) # 94 days, 4:00:20
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
