"""
intermediate_assignment_90:

Write a Python program to get a year from user to check it is leap year or not using OOP

"""
class Check:
    def __init__(self):
        print("Hello")
        
    @classmethod
    def check_leap_year(cls, year):
        cls.year = int(year)
        if cls.year %4 ==0:
            print(str(year)+" is a leap year")
        else:
            str(year)+" is not a leap year"
            
            
year = input("Enter the year : ")

Check.check_leap_year(year)