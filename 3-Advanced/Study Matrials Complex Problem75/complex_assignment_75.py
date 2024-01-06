
"""
complex_assignment_75:

Write Desktop application in Python Program To Find Force Of A Man On A Object Which Have  Mass And Acceleration.
Get Mass And Acceleration From User

f = m * a
"""

from tkinter import *

def get_Force():
    Force = float(Mass.get()) * float(Acceleration.get())
    Force_label = Label(window, text = "Force = "+str(Force)+"n")
    Force_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Add half")

Mass = Entry(window, width=50)
Mass.pack()
Acceleration = Entry(window, width=50)
Acceleration.pack()

btn = Button(window, text="Result", command= get_Force).pack()


window.mainloop()