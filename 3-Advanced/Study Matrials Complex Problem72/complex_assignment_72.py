"""
complex_assignment_72:

Write Desktop Application in Python To Get 2 Number From The User, Find Their Square, And Add Both Result,
Finally Find Cube Of Result And Display To User.

"""

from tkinter import *

def get_total_square_and_cube():
    total_square = int(num1.get())**2 + int(num2.get())**2
    total_square_label = Label(window, text = "total_square = "+str(total_square))
    total_square_label.pack()
    cube = total_square**3
    cube_label = Label(window,  text = "total_square_cube = "+str(cube))
    cube_label.pack()
    


window = Tk()
window.geometry("500x500")
window.title("sum of square of 2 Numbers")

num1 = Entry(window, width=50)
num1.pack()
num2 = Entry(window, width=50)
num2.pack()


btn = Button(window, text="Result", command= get_total_square_and_cube).pack()


window.mainloop()