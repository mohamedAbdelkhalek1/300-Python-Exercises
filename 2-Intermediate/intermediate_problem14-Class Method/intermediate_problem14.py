
"""
intermediate_problem14:

Write a Python program to create a class of student having two data member (name and id) having a two methods,
one is used to get name and id and other is to display name and id to user.   

"""

class Jafri:
    def __init__(self):
        self.name = None
        self.u_id = None

    def getData(self):
        self.name = input("Enter your name")
        self.u_id = input("Enter your id")
    
    def show(self):
        print(self.name)
        print(self.u_id)
    
obj = Jafri()
obj.getData()
obj.show()