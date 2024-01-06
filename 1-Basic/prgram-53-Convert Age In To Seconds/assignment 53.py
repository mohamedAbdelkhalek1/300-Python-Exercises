"""
siignment 53:

Write A Python Program To Get Age From The User In Year, And Convert Age In To Seconds, minutes and hours 

"""



"""
1 day = 24H
One year = 365 * 24 = 8760 H
1H = 60 M
One year = 8760 * 60 M = 525600 M
IH = 3600s
8760 H into s?
8760 * 3600 = 31536000s
"""

age = float(input("Enter your age : "))
age_in_hour = 8760 * age
age_in_min = 525600 * age
age_in_sec =  31536000 * age

print("Your age is "+str(age))
print("Your age in seconds is "+str(age_in_sec))
print("Your age in Minutes is "+str(age_in_min))
print("Your age in houres is "+str(age_in_hour))