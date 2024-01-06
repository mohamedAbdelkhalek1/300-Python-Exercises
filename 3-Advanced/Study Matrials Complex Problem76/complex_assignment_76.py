
"""
complex_assignment_76:

Write Desktop application in  A Python Program To Add Number From List That Are Greater Than 5 And Less Than 10

"""

from tkinter import *

def get_Force():
    result = [i for i in my_list if 10>i>5]
    result_label = Label(window, text = "result = "+str(result))
    result_label.pack()

my_list = [5,7,1,4,6,8,3,24,2]

window = Tk()
window.geometry("500x500")
window.title("lst")


btn = Button(window, text="Result", command= get_Force).pack()


window.mainloop()