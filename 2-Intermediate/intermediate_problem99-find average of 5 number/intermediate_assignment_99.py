"""
intermediate_assignment_99:

Write a Python Program to find average of 5 number using OOP.

"""
class Average:
    def get_numbers(self):
        self.sum = 0
        for i in range(5):
            num = int(input(f"Enter number {i+1} : "))
            self.sum += num
        print("Total ="+str(self.sum))
            
    def get_avrg(self):
        self.avrg = self.sum / 5
        print("Average ="+str(self.avrg))
        
obj = Average()
obj.get_numbers()
obj.get_avrg()