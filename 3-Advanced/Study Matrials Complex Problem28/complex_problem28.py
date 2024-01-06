"""
complex_problem28:

Write a Python Program to Rotate an image

"""

from PIL import Image

img = Image.open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem28/image.png")
angle = int(input("Enter a angle"))
rotated_img = img.rotate(angle)
rotated_img.show()