"""
complex_assignment_86:

Create a Desktop Application in a Python that displays a dialog box asking the user to enter an integer and
    display its square in Window

"""
from tkinter import *
from tkinter import simpledialog

window = Tk()
window.title("Square")
window.geometry("500x500")

number = simpledialog.askinteger("Input", "Enter a number : ")

sqr = number*number

label = Label(window, text="Square of number = "+str(sqr))
label.pack()

window.mainloop()