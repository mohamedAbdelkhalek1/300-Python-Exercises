"""
intermediate_assignment_79:

Create a Desktop Python program to create a window and provide title with icon.

"""

from tkinter import * 
root = Tk()
root.geometry("500x500")


root.title("Window Title Example...")

# Set the window icon
icon = PhotoImage(file="E:/bulding/python_exercises/2-Intermediate/intermediate_problem79-/R.png")  # Provide the path to your icon image file
root.iconphoto(True, icon)

root.mainloop()