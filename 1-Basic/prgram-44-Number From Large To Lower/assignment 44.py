"""
assignment 44:

Write A Python Program To Get Large Number As Starting And Lower Number As Ending Number,
Display That Number From Large To Lower And Find Their Sum.

"""

s = int(input("Enter start number, that is larger"))
e = int(input("Enter end number, that is lower"))

sum = 0
for i in range(s,e-1,-1):
    print(i)
    sum += i
    
print("Sum = "+str(sum))