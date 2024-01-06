"""
problem 14 :

Write a program to get 6 number in the TUPEL and sum that number 


"""




# to get 6 number 
# store to list
# convert the list into a tuble
# sum and dispaly resutl to user

lst = []
# to get number from the user and store to list
for i in range(6): # 0 1 2 3 4 5
    lst.append(int(input(f"Enter item number {i+1} : ")))

# To convert the list into a tuble
tbl = tuple(lst)
print("the tuble : ",tbl)

# To sum number of the tuble
print("Sum of number in the tuble : ",sum(tbl))


