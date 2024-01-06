"""
assignment 30:

Write A Python Program To Get A  Number From User To Check, It Is Divisible By 5 And 6


"""


# # to get a number 
# # divisbile by 5 and 6

num = int(input("Enter the number : "))

if num%5==0 and num%6 ==0:
    print("It Is Divisible By 5 And 6")
else:
    print("It Is Not Divisible By 5 And 6")