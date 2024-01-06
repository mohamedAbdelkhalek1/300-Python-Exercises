"""
intermediate_assignment_101:

Write a Python Program to find addition of list element to create a new list. Add element of list as 1st and 2nd….  Using OOP.

"""
class Addition:
    def put_array(self):
        self.lst = []
        n = int(input("Enter a length of the list "))
        for i in range(n):
            item = int(input(f"Enter a number {i+1} : "))
            self.lst.append(item)
        print(self.lst)
        
    def get_addition(self):
        self.new_list = []
        n = len(self.lst)
        for i in range(n-1): # 6
            item = self.lst[i] + self.lst[i+1]
            self.new_list.append(item)
        print(self.new_list)
        
add1 = Addition()
add1.put_array()
add1.get_addition()