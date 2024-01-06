"""
assignment 63:

Write A Python Program To Find Minimum Number From A List Using Function 

"""


def min_num(lst):
    min = 0
    for i in lst:
        if i < min:
            min = i
    return min

lst = []

for i in range(10):
    lst.append(int(input(f"Enter number {i+1} : ")))

min = min_num(lst)
print(min)





# # different function with min()

# def min_num(l):
#     #print(type(l))
#     print(min(l))
# min_num(lst)