"""
problem 63:

Write A Python Program To Find Maximum Number From A List Using Function 

"""


# To ge 10 number, store in the list
# Pass to function
# find max number

def max_num(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

lst = []

for i in range(10):
    lst.append(int(input(f"Enter number {i+1} : ")))

max = max_num(lst)
print(max)







# # different function with max()

# def max_num(l):
#     #print(type(l))
#     print(max(l))
# max_num(lst)