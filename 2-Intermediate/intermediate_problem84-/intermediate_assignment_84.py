"""
intermediate_assignment_84:

Write a Desktop Python program to create a Checkboxes to change background color, cursor, font, fg, border etc.

"""

import tkinter as tk

def apply_changes():
    if checkbox_bg_var.get():
        root.config(bg='yellow')
    else:
        root.config(bg='white')

    if checkbox_cursor_var.get():
        root.config(cursor='pirate')
    else:
        root.config(cursor='arrow')

    if checkbox_font_var.get():
        root.config(font=('Arial', 12))
    else:
        root.config(font=('TkDefaultFont', 12))

    if checkbox_fg_var.get():
        root.config(fg='red')
    else:
        root.config(fg='black')

    if checkbox_border_var.get():
        root.config(bd=5, relief='solid')
    else:
        root.config(bd=0, relief='flat')

root = tk.Tk()
root.title("Visual Properties")

checkbox_bg_var = tk.BooleanVar()
checkbox_bg = tk.Checkbutton(root, text="Background Color", variable=checkbox_bg_var)
checkbox_bg.pack()

checkbox_cursor_var = tk.BooleanVar()
checkbox_cursor = tk.Checkbutton(root, text="Cursor", variable=checkbox_cursor_var)
checkbox_cursor.pack()

checkbox_font_var = tk.BooleanVar()
checkbox_font = tk.Checkbutton(root, text="Font", variable=checkbox_font_var)
checkbox_font.pack()

checkbox_fg_var = tk.BooleanVar()
checkbox_fg = tk.Checkbutton(root, text="Foreground Color", variable=checkbox_fg_var)
checkbox_fg.pack()

checkbox_border_var = tk.BooleanVar()
checkbox_border = tk.Checkbutton(root, text="Border", variable=checkbox_border_var)
checkbox_border.pack()

apply_button = tk.Button(root, text="Apply Changes", command=apply_changes)
apply_button.pack()

root.mainloop()