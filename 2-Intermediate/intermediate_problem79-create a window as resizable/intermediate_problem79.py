"""
intermediate_problem79:

Create a Desktop Python program to create a window as resizable.

"""

from tkinter import * 
root = Tk()
root.title("Window Title Example...")
root.geometry("500x500")
root.resizable(True, False)   #can change a widgth only
root.mainloop()