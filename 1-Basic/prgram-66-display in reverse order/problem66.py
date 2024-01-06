
"""
Problem 66:

Write A Python Program To Create A List To Pass To Function As A parameter To Display Its Element In Reverse Order. 

"""


#create the list
lst = [5,7,6,1,2,8]

#create a reverse function
def rev_lst(lst):
    lst.reverse()
    print(lst)
    

rev_lst(lst)