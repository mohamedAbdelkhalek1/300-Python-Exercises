"""
assignment 21:

Write a Python Program to get 5 number from user in array, find the Minimum number


"""


# get 5 number from the user
# store in the array and display 
# find min

import array as arr

a = arr.array('i',[])

for i in range(5): 
    a.append(int(input("Enter a number to store in the array")))
m = a[0] # 2,3,4,5,6
for j in range(5):
    print(a[j])
    if(a[j] < m):
        m = a[j]
print("Min Number = "+str(m))
