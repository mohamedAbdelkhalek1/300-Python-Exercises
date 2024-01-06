
"""
problem 51:

Write Python Program To Find Number Of Day Between Two Dates

"""




from datetime import datetime

date1 = input("Enter 1st date \n in this formate d/m/Full year")
date2 = input("Enter 2nd date \n in this formate d/m/Full year")

date_format = "%d/%m/%Y"

d1 = datetime.strptime(date1, date_format)
d2 = datetime.strptime(date2, date_format)
diff  = d2-d1
print(diff.days * 24)