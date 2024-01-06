"""
assignment 27:

Write A Python Program To Get 5 Year From The User To Store In Array And Display Only Leap Year To User


"""


normal_year = []
leep_year = []

for i in range(5):
    normal_year.append(int(input(f"Enter year {i+1} : ")))
    if normal_year[i] % 4 ==0 :
        leep_year.append(normal_year[i])
        
print(f"Normal years : {normal_year}")
print(f"leep years : {leep_year}")