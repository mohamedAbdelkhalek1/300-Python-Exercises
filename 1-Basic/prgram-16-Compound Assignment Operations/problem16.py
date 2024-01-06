"""
problem 16:

Write A Program That Performs All Compound Assignment Operations On An Integer

"""


"""
Compound Assignment Operations:

Compound assignment operations, or augmented assignment operators,
are shorthand operators in programming languages that combine an arithmetic or bitwise operation with an assignment in a single expression.

These operators perform an operation on the variable's value and assign the result back to the same variable.

+=: Addition assignment. Example: x += 5 is equivalent to x = x + 5.
-=: Subtraction assignment. Example: y -= 3 is equivalent to y = y - 3.
*=: Multiplication assignment. Example: z *= 2 is equivalent to z = z * 2.
/=: Division assignment. Example: a /= 4 is equivalent to a = a / 4.
%=: Modulus assignment. Example: b %= 7 is equivalent to b = b % 7.

"""




# To get a integer from the user
# perform compound assignment operators

num = int(input("Enter a integer")) #'4' -> 4
#num = 4
# addition assignment operator
num += 5 # num + 5 -> 4 + 5 ->num
print(num) # 9

# Subtraction assignment operator
num -= 5 # num - 5 -> 4 - 5 ->num
print(num) # 4

# Mulitplication assignment operator
num *= 5 # num * 5 -> 4 * 5 ->num
print(num) # 20

# Division assignment operator
num /= 5 # num / 5 -> 20 / 5 ->num
print(num) # 4


# Mod assignment operator
num %= 5 # num / 5 ->4 % 5 ->num
print(num) # 4





