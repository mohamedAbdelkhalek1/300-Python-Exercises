"""
intermediate_assignment_9:

Write A Python Program Sort Dictionary By Value

"""

dict = {"Name":"Faisal","Course":"Python","City":"DIKHAN"}
print(dict)


sorted_dict = sorted(dict.items(), key=lambda x: x[1])

        
print("Sort Dictionary By Value : ", sorted_dict)


#should value in the same data type
#We use the sorted() function with the key parameter set to lambda x: x[1] 
#    to specify that we want to sort the dictionary based on its values.