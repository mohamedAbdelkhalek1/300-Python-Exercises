"""
assignment 89:

Write A Python Program To Generate Number From 0 To 20 Only Divisible By 3 Number And  Generate 0 To 20 Only Divisible By 5.
Add Both Generated Number To Each Other To Display Total Result 


"""
s1 = 0
s2 = 0
for i in range(0,21):
    if (i%3 == 0):
        s1 += i
        print(i)
print("Divisible By 3 Number = "+str(s1))

for i in range(0,21):
    if (i%5 == 0):
        s2 += i
        print(i)
print(" Divisible By 5 number = "+str(s2)) 
print("Total result is = "+str(s1+s2))   