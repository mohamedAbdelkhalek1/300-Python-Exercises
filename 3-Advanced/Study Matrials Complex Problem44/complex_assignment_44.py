"""
complex_assignment_44:

Display image using other than PIL library.

"""
import cv2

img = cv2.imread("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem44/image.png")

cv2.imshow("Image", img)

cv2.waitKey(0)
