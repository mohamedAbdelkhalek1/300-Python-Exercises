
"""
complex_assignment_74:

Write A Desktop application in  Python Program To Find Acceleration Of An Object Having Velocity v in t Time. 

a = v / t

"""

from tkinter import *

def get_acceleration():
    acceleration = float(velocity.get()) / float(time.get())
    acceleration_label = Label(window, text = "Acceleration = "+str(acceleration)+"m/s2")
    acceleration_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Add half")

velocity = Entry(window, width=50)
velocity.pack()
time = Entry(window, width=50)
time.pack()

btn = Button(window, text="Result", command= get_acceleration).pack()


window.mainloop()