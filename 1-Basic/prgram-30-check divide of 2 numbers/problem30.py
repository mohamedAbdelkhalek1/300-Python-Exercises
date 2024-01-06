"""
problem 30:

Write A Python Program To Get A  Number From User To Check, It Is Divisible By 2 And 3

"""



# # to get a number 
# # divisbile by 2 and 3

num = int(input("Enter the number : "))

if num%2==0 and num%3 ==0:
    print("It Is Divisible By 2 And 3")
else:
    print("It Is Not Divisible By 2 And 3")