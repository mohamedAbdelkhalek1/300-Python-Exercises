"""
complex_problem27:

Write a Python Program to Blur an image.

"""


import cv2
img = cv2.imread("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem27/image.png")
blur_Image = cv2.blur(img,(100,10))
cv2.imshow("Title of real image", img)
cv2.imshow("Title image", blur_Image)
cv2.waitKey(0)
