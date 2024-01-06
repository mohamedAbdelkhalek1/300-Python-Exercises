"""
complex_assignment_71:

Write A Desktop application in Python to get 3 subject marks from the user and calculate total and average of that marks.
And display to user.

"""
from tkinter import *

def get_total_and_avarage():
    total = int(mark1.get()) + int(mark2.get()) + int(mark3.get())
    avg = total / 3
    total_label = Label(window, text = "total = "+str(total))
    total_label.pack()
    avg_label = Label(window, text = "average = "+str(avg))
    avg_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Calculate marks")

mark1 = Entry(window, width=50)
mark1.pack()
mark2 = Entry(window, width=50)
mark2.pack()
mark3 = Entry(window, width=50)
mark3.pack()

btn = Button(window, text="Result", command= get_total_and_avarage).pack()


window.mainloop()