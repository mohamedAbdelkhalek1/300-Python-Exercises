"""
complex_assignment_5:

Write A Python Program To Find Union , Intersection And Difference Of Two Set.
Find Sum Of All Items Of Union, Intersection And Difference.

"""
a = set()
b = set()

for i in range(5):
    a.add(int(input(f"Enter a element {i+1} : ")))

for i in range(5):
    b.add(int(input(f"Enter b element {i+1} : ")))

u = a.union(b)
print("Union of two set is  "+str(u))
print("sum of Union = "+str(sum(u)))


i = a.intersection(b)
print("Intersection of two set is  "+str(i))
print("sum of Intersection = "+str(sum(i)))



d = a.difference(b)
print("Difference of two set is  "+str(d))
print("sum of Difference = "+str(sum(d)))
