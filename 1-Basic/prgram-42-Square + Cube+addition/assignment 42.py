"""
assignment 42:

Write A Python Program To Generate 10 To 1 Number (Having 4 Difference) With Their Square And Cube And Also Display Their Addition (Square + Cube)
Expected result:
Number 	Square		Cube 		Addition
10		 100		 1000		11,00 
6		 36		 216		252
2		 4	  	 8		12

"""


print("Number\t\t Square\t\t Cube\t\t Addition")
for i in range(10,0,-4):  
    print(str(i)+"\t\t"+str(i*i)+"\t\t"+str(i*i*i)+"\t\t"+str((i*i)+(i*i*i)))









#another way
# print("Number\t\t Square\t\t Cube\t\t Addition")
# for i in range(-10,1,4):  
#     print(str(abs(i))+"\t\t"+str(abs(i*i))+"\t\t"+str(abs(i*i*i))+"\t\t"+str(abs(i)+abs(i*i*i)))
    
    
    
    
