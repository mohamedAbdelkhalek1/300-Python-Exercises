"""
complex_problem26:

Write a Python Program to find resolution of an image

"""

import cv2
img = cv2.imread("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem26/image.png")
h = img.shape[0] # height
w = img.shape[1] # width 
print(h)
print(w)
print("resolution = ", str(w) +" x "+str(h), "Pixel")