"""
problem 20:

Write A Python Program To Get 5 Number From User In Array And Sum All Number And Display


"""






# get 5 number from the user
# store in the array and display 
# find their sum 

from array import array

a =array('i',[])     
s = 0
for i in range(5):#0 to 4 
    a.append(int(input(f"Enter a number {i+1} to store in the array : ")))
for j in range(5):#0 to 4 
    print(a[j])
    s += a[j] # 2,3,4,5,6,7
print("Sum of the number is = "+str(s))



#can use sum() bult in function
#print(sum(a))