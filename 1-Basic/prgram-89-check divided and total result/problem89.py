"""
problem 89:

Write A Python Program To Generate Number From 0 To 20 Only Even Number And  Generate 0 To 20 Odd Number.
Add Both Generated Number To Each Other To Display Total Result 


"""

# to gen even, 0 to 20
# add even
# to gen odd, 0 to 20
# add odd 
# add even + odd
s1 = 0
s2 = 0
for i in range(0,21):
    if (i%2 == 0):
        s1 += i
        print(i)
print("Even number = "+str(s1))

for i in range(0,21):
    if (i%2 != 0):
        s2 += i
        print(i)
print("Odd number = "+str(s2)) 
print("Total result is = "+str(s1+s2))     


# #Another solution
# even_num = list(range(0,21,2)) 
# sum_even = sum(even_num) 
# print("Even number = "+str(sum_even))

# odd_num = list(range(1,21,2)) 
# sum_odd = sum(odd_num) 
# print("odd number = "+str(sum_odd))

# print("Total result is = "+str(sum_even+sum_odd))