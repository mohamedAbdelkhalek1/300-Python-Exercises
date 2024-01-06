"""
intermediate_assignment_81:

Create a Desktop Python Program to insert a Button in Window.
When click on the button, it take two number from user to add both number in console.

"""
from tkinter import *
 
root = Tk()
root.title("Button clicking...")
root.geometry("300x300")

def myfunc():
    num1 = input("Enter number 1")
    num2 = input("Enter number 2")
    print(f"{num1} + {num2} = {num1+num2}")

btn = Button(root, text="Click me", command=myfunc)
btn.pack()
root.mainloop()