"""
assignment 99:

Write A Python Program To Get Only Lowercase Words From User To Store In A List 

"""

lst = []
for i in range(10): # 0 to 9
    w = input("Enter word to store in list")
    if(w.islower()):
        lst.append(w)
    else:
        print("Error! Insert lowercase word")
print(lst)