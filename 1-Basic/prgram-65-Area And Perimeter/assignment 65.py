"""
assignment 65:
Write A Python Program To Find Area And Perimeter Of A Square Using Function 
       (A = L2, P = 4a), Find Square Root Of Its Area And Perimeter And Add Both Result. And Display Final Result To User

"""

import math

l = float(input("Enter lenght of square"))

def area_peri_sumOfSquareRoot(lenght):
    area = lenght*lenght
    perimeter = 4*lenght
    print("Area = "+str(area))
    print("Perimeter = "+str(perimeter))
    print("Square Root Of Area = "+str(math.sqrt(area)))            #can get with area**.5
    print("Square Root Of Perimeter = "+str(math.sqrt(perimeter)))


area_peri_sumOfSquareRoot(l)