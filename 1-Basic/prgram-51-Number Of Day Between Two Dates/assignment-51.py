"""
assignment-51:

Write Python Program To Find Number of Hours Between Two Dates


"""
from datetime import datetime as dt

format_date = "%d/%m/%Y"

date1 = dt.strptime(input("Enter date 1 as Day/Month/Year"),format_date)
date2 = dt.strptime(input("Enter date 1 as Day/Month/Year"),format_date)

diff_hour  = (date2-date1).days * 24
#or -->  diff_hour  = (date2-date1).total_seconds() / 3600

print("Hours Between Two Dates : ",diff_hour)