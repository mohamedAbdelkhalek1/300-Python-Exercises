"""
assignment 66:

Write A Python Program To Display only Prime Number from A Given Number.

"""

def check_prime(num):
    counter = 0

    lis = range(2,10)

    for i in lis:
        if num < 10:
            if num %i == 0 :
                counter += 1
        else:
            if num %i == 0 :
                counter += 2
    if num == 1:
        return False
    else:
        if counter < 2:
           return True
        else:
           return False
            



lst = range(30)

for i in lst:
    if check_prime(i):
        print(i)
        





# #another solution
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def display_prime_numbers(n):
#     primes = []
#     for num in range(2, n + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# # Example usage
# given_number = int(input("Enter a number: "))
# prime_numbers = display_prime_numbers(given_number)
# print("Prime numbers:", prime_numbers)