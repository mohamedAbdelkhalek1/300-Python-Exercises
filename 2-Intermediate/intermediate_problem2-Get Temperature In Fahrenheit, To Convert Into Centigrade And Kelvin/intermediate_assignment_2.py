"""
intermediate_assignment_2:

Write A Python Program To Get Temperature In Centigrade, To Convert Into Fahrenheit And Kelvin 

"""
#Formula F to C(°F − 32) × 5/9 = °C
#Formula F to K(32°F − 32) × 5/9 + 273.15 = 273.15K


c = float(input("Enter temp in C : "))
# f = c * 9/5 + 32
#k = c + 273.15  

c_to_f = c * 9/5 + 32
print("Temp is converted from c to f "+str(c_to_f)+"\n")


c_to_k = c + 273.15
print("Temp is converted from c to K "+str(c_to_k))

