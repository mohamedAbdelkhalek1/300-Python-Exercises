"""
intermediate_problem34:

Write a Python OOP program to get a number from user to display its table. 

"""


class Table:
    def getNum(self):
        self.num = int(input("Enter a number"))

    def showTable(self):
        for i in range(1,11):
            # 1 *2 = 2
            # 2 * 2 = 4
            # 3 * 2 = 6
            print(str(i)+" * "+str(self.num)+" = "+str(i*self.num))

obj = Table()
# obj.getNum()
# obj.showTable()