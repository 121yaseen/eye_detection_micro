import cv2
import numpy as np

cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


img = cv2.imread('groupfie.jpg')
img = cv2.resize(500, 500)
copy = img.copy()
gray = cv2.