"""
complex_assignment_49:

Write a Python Program for Binary Search

"""
# Binary Search is a search used in a sorted array 

array = [1,2,4,5,14,53] # 6
item = int(input("Enter a element"))
n = len(array)
ind = 0
element = 0
flg = False

l = 0
h = n-1
while l<=h:
    mid = (l+h) //2
    if item < array[mid]:
        h = mid-1
    elif item > array[mid]:
        l = mid+1
    else:
        ind = mid
        element = array[mid]
        flg = True
        break
    
if flg:
    print("Element is Existed, at "+str(ind)+" index that is "+str(element))
else:
    print("Not found")