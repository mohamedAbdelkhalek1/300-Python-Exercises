"""
complex_assignment_28:

Write a Python Program to Rotate an image: Using another method

"""
import cv2

img = cv2.imread("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem28/image.png")

rotate_img = cv2.rotate(img, 80)

cv2.imshow("Image", rotate_img)

cv2.waitKey(0)
