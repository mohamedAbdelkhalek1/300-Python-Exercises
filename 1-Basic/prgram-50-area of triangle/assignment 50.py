
"""
assignment 50:

Write A Python Program To Find Area Of Triangle And
Then Get A Number From The User, Find Square Of That Number.
Then Add With Area Of The Triangle.
Total Result Display To User


"""

# to get base and height from the user
# find area of the triangle 

b = float(input("Enter Base "))
h = float(input("Enter Height "))

num = int(input("Enter number to get sqare : "))

area_traingle = (b * h)/2
num_sqare = num**2

print("Area of the triangle is = "+str(area_traingle))
print("sqare of the number is = "+str(num_sqare))
print("Total Result  = "+str(num_sqare + area_traingle))

