
"""
problem 35:

Write A Python Program To Get 10 Name Of The Students From The User In A List, Display That Students Name In Descending Order


"""

# to get 10 student name
# dispaly in desc order

std_name = []

for i in range(10):
    std_name.append(input(f"Enter name of the Student {i+1} : "))
#print("These are student stored in the list "+str(std_name))

print("Student Name in proper form")
for j in std_name:
    print(j)

std_name.reverse()

print("Student Name in DESC form")
for d in std_name:
    print(d)



# #can use sorted() function to print sort of the list without changing in the original list
# print(sorted(std_name,reverse=True))