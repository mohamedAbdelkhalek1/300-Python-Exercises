"""
intermediate_problem77:

Create a Desktop Python program to create a window and set its title.

"""

from tkinter import * 
import webbrowser


def open():
    webbrowser.open("https://poe.com/")

window = Tk()

window.title("Window")
window.geometry("500x500")

#Create button
button1 = Button(window, text="Click", bg="yellow", fg="#4281f5", font="Helvetica 20 bold", padx=10, pady=4, 
                 command=open)
button1.pack(side = TOP)

window.mainloop()