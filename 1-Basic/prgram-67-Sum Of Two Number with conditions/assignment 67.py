"""
assignment 67:

Write A Python Program To Find Sum Of Two Number 
(1st Number Should Be Positive And 2nd Number Should Be Negative And Less Than 50 And Greater Than 20)

"""


num1 = int(input("Enter 1st num : "))
num2 = int(input("Enter 2nd num : "))

if((num1>0 and num2<0) and (20<num1<50 and 20<abs(num2)<50)):
    print("Addition of both numer is "+str(num1+num2))
else:
    print("1st Number Should Be Positive And 2nd Number Should Be Negative And Less Than 50 And Greater Than 20")