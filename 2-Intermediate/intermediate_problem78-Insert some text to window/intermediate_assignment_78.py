"""
intermediate_assignment_78:

Create a Desktop Python program to create a window and Insert some text to window. Also change label color, background color etc

"""
from tkinter import *

window = Tk()

window.title("Window 1")
window.geometry("500x500")

txt = Label(window, text="Hello World", bg="red", fg="#4281f5", font="Helvetica 20 bold", padx=10, pady=4)
txt.pack(pady=30)


window.mainloop()