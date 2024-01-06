"""
assignment 16:


Write A Program That Performs All Compound Assignment Operations On An Integer. And Add All The Result, And Then Display To User.



"""


# To get a integer from the user
# perform compound assignment operators
# add all the results


sum = 0
num = int(input("Enter a integer")) #'4' -> 4
#num = 4
# addition assignment operator
num += 5 # num + 5 -> 4 + 5 ->num
sum += num
print(num) # 9

# Subtraction assignment operator
num -= 5 # num - 5 -> 4 - 5 ->num
sum += num
print(num) # 4

# Mulitplication assignment operator
num *= 5 # num * 5 -> 4 * 5 ->num
sum += num
print(num) # 20

# Division assignment operator
num /= 5 # num / 5 -> 20 / 5 ->num
sum += num
print(num) # 4


# Mod assignment operator
num %= 5 # num / 5 ->4 % 5 ->num
sum += num
print(num) # 4

print(f"Sum of all results = {sum}")