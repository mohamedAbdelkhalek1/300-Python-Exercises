
"""
complex_assignment_78:

Write Desktop application in A Python To Sort Student Name In Ascending Order In List And Student Should Display Which
    Contain Only 5 Character

"""

from tkinter import *

def student_name():
    result = [i for i in my_list if len(i)==5]
    sort_res = sorted(result)
    result_label = Label(window, text = "result = "+str(sort_res))
    result_label.pack()

my_list = ["Ahmed", "Sara", "Mohammed","Saleh"]

window = Tk()
window.geometry("500x500")
window.title("Student Name")


btn = Button(window, text="Result", command= student_name).pack()


window.mainloop()

