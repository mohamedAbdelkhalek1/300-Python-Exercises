"""
complex_assignment_9:

Write A Python Program To Get 5 Items From A List That Are Divisible By 5 And 7, Not Included Last And First Item

"""
lst = []

for i in range(5):
    lst.append(int(input(f"Enter a item {i+1} : ")))

for x in lst[1:4]:
    if x%5==0 and x%7==0:
        print(x)