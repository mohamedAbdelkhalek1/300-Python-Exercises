"""
complex_assignment_73:

Write A Desktop application in Python Program To Get A Number From User, The System Should Add Auto Increment To That Number.
Half Of User Entered Number Should Be Incremented 


"""

from tkinter import *

def add_half():
    result = int(num1.get()) + int(num1.get())/2
    result_label = Label(window, text = "total_result = "+str(result))
    result_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Add half")

num1 = Entry(window, width=50)
num1.pack()

btn = Button(window, text="Result", command= add_half).pack()


window.mainloop()