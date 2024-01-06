"""
problem 23:

Write a Python program get name of week and show “Holiday” if user input Sunday


"""



# to get week name
# sunday, then display it is holiday

week_name  = input("Enter a week name ")

if(week_name == 'Sunday' or week_name == 'Sun' or week_name == 'sun'or  week_name == 'sunday' ):
    print("It is holiday") 
else:
    print("It is not Holiday")




# #another solution with list
# day = input("Enter name of day : ")
# if day in ["Sunday","sunday","Sun","sun"] :
#     print("Holiday")