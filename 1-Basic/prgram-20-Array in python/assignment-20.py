"""
assignment 20:

Write a Python Program to get 5 number from user in array, AND find maximum number.


"""

from array import array

a =array('i',[])     
max = 0
for i in range(5):#0 to 4 
    a.append(int(input(f"Enter a number {i+1} to store in the array : ")))
    if i==0:
        max = a[i]
    else:
        if a[i]>max:
            max = a[i]

print("maximum number : ",max)




