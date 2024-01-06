"""
problem 15:

Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display


"""


# get six number from the user
# display 
# clear list
# then display

lst = []
# to get number from the user and store to list
for i in range(6): # 0 1 2 3 4 5
    lst.append(int(input(f"Enter number {i+1} : ")))

print("This is the list")
print(lst)
lst.clear()
print("We have removed the list items")
print(lst)