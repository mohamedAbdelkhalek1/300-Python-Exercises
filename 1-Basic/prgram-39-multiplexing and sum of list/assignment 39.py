"""
assignment 39:

Write A Python Program To Get 5 Number In The TUPLE, Pass That TUPLE In The Function 
To Multiply And Add That Number And Display Total Result. 


"""

tpl = ()

for i in range(5): # 0 1 2 3 4
    tpl= tpl + (int(input("Enter a number to store in the tuple : ")) , )
print(tpl)

def add_mul(tpl_num):
    s = 0
    m =  1
    for i in tpl_num:
        s += i
        m *= i  
    print("Addition = "+str(s))
    print("Multiplicaiton = "+str(m))
    
add_mul(tpl)

    
 #use a concatination to add item to tuple
 #can convert to list then return   