"""
problem 15:

Write A Program To Get 6 Number In The TUPLE And Display All Number And Then Clear TUPLE And Then Display


"""


# # get six number from the user
# # display as a tuble
# #return to list
# # clear list
# # then display as atuble

# lst = []
# # to get number from the user and store to list
# for i in range(6): # 0 1 2 3 4 5
#     lst.append(int(input(f"Enter number {i+1} : ")))
    
# tbl = tuple(lst)

# print("This is the tuble")
# print(tbl)
# lst.clear()  #this mean make list empty, but del(lst) means delete the list  
# tbl = tuple(lst)

# print("We have removed the tuble items")
# print(tbl)



# #another solution by concatenation
# numbers = ()
# for i in range(6):
#     num = int(input("Enter a number: "))
#     numbers += (num,)

# print("Numbers in the tuple:", numbers)

# numbers = ()
# print("Tuple cleared!")

# print("Numbers in the cleared tuple:", numbers)