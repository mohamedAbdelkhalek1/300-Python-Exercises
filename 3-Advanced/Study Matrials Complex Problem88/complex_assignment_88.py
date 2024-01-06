"""
complex_assignment_88:

Write a Desktop Application in Python to create a Listbox widget to perform different methods.

"""
from tkinter import *

def method1():
    l1 = Label(window, text="Method 1 called")
    l1.pack()

def method2():
    l2 = Label(window, text="Method 2 called")
    l2.pack()

def method3():
    l3 = Label(window, text="Method 3 called")
    l3.pack()

def perform_action():
    selected_item = listbox.get(listbox.curselection())
    if selected_item == "Method 1":
        method1()
    elif selected_item == "Method 2":
        method2()
    elif selected_item == "Method 3":
        method3()

# Create the main window
window = Tk()
window.title("Listbox Application")

# Create a Listbox
listbox = Listbox(window)
listbox.pack()

# Add items to the Listbox
listbox.insert(0, "Method 1")
listbox.insert(1, "Method 2")
listbox.insert(2, "Method 3")

# Create a button to perform the selected action
button = Button(window, text="Perform Action", command=perform_action)
button.pack()

# Start the main event loop
window.mainloop()