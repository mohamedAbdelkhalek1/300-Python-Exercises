"""
assignment 54:

Write A Python Program To Get A Number From The User To Find Factorial Of That Number. Using another method as I discussed

"""
def get_factorial(number):
    fac = 1
    for i in range(1,number+1):
        fac *= i
        
    return fac


num = int(input("Enter a number to find its factorial"))

fac_of_no = get_factorial(num)

print("Your number is "+str(num))
print("Factorial of "+str(num)+" is "+str(fac_of_no))
