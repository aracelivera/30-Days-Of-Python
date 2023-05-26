#   Day 16 - Date Time


# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime 
current_date = datetime.now()
print('current day: ', current_date)
print(f'day= {current_date.day}\nmonth= {current_date.month}\nyear= {current_date.year}\nhour= {current_date.hour}\nminute= {current_date.minute}\ntimestap= {current_date.timestamp()}')

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(current_date.strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.
time_string = '5 December, 2019'
time = datetime.strptime(time_string, "%d %B, %Y")
print(time) # 2019-12-05 00:00:00

# 4. Calculate the time difference between now and new year.
new_year= datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0)
print('Time left for new year:', new_year- current_date) 

# 5. Calculate the time difference between 1 January 1970 and now.
from datetime import date
old_date= date(year=1970, month=1, day=1)
diff= date.today() - old_date
print('Difference between 1 January 1970 and now:', diff)