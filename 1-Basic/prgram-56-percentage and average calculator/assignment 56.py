"""
assignment 56:

Write A Python Program To make a average calculator. 

"""

# To get terms
# to get value of that terms
# total/terms
term = int(input("Enter total terms")) # 4

lst = []
s = 0

for i in range(term):
    lst.append(int(input(f"Enter terms {i+1} : ")))
    s += lst[i]
#print(lst)

print("You entered "+str(term)+" terms")
print("Total of terms values is "+str(s))
print("Average is equal to "+str(s/term))
