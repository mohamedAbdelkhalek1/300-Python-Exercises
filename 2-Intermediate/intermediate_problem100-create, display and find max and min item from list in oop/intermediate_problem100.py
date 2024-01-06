"""
intermediate_problem100:

Write a Python Program to create a list on run time, display list element, and also find max and min item from list of integers using OOP.

"""

class MinMax:
    def getList(self):
        self.lst = []
        for i in range(5):
            self.item = int(input(f"Enter number {i+1} : "))
            self.lst.append(self.item)
    
    def showList(self):
        print(self.lst)
    
    def minmax(self):
        print("Max = "+str(max(self.lst)))
        print("Min = "+str(min(self.lst)))

obj = MinMax()
obj.getList()
obj.showList()
obj.minmax()