"""
Assignment 1:

Write A Python Program To Show Such Type Of Layout Of Number, Square And Cube.
Expected Result:
Number 		Square 			Cube 
1			1			1
2			4			8
3			9			27
4			16			64
5			25			125

    
    
"""





# #simple solution:

# print("Number \t\t Square \t\t cube")
# print("1 \t\t "+str(1*1)+" \t\t "+str(1*1*1)) 
# print("2 \t\t "+str(2*2)+" \t\t "+str(2*2*2)) 
# print("3 \t\t "+str(3*3)+" \t\t "+str(3*3*3)) 
# print("4 \t\t "+str(4*4)+" \t\t "+str(4*4*4)) 
# print("5 \t\t "+str(5*5)+" \t\t "+str(5*5*5)) 






# #Advanced solution

# print("Number \t\t Square \t\t cube")
# for i in range(1,6):
#     print(f"{i} \t\t\t {i*i} \t\t\t {i*i*i}")