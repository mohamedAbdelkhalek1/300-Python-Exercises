"""
complex_assignment_90:

Write Desktop application in A Python To Get A Number From The User To Find Factorial Of That Number

"""
from tkinter import *
import math

def get_factorial():
    fac = math.factorial(int(num.get()))
    fac_label = Label(window, text=str(fac))
    fac_label.pack()

window = Tk()
window.geometry("500x500")
window.title("Factorial Of That Number")

num = Entry(window, width= 50)
num.pack()

btn = Button(window, text="Factorial", command= get_factorial)
btn.pack()

window.mainloop()