"""
problem 80:

Write A Python Program To Print Characters From A String That Are Present At An Odd Index Number

"""


# to get sentence
# display char of odd index number

s = input("Enter a sentence")
s_len = len(s)
#print(s_len)
for n in range(1,s_len):
    if(n%2!=0):
        print(s[n])


# #Another solution
# s = input("Enter a sentence : ")
# print(s[1::2])