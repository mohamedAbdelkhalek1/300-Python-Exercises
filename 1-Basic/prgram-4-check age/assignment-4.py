"""
assignment 4:

Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not.
If Marks Is Less Than 60 Then It Don’t Allow To Take Admission. 

Expected Result if user input 50 year then:
Sorry! You cannot take admission, you need 10 numbers more to take admission




"""


name =input("Enter your name : ")

mark = int(input("Enter your age : "))

if mark >= 60 :
    print(f"Hi {name} You can take admission")
else:
    print(f"Sorry! You cannot take admission, you need {60 - mark} numbers more to take admission")