import cv2
import numpy as np


kernel = np.ones((5,5), np.uint8)
print(kernel)

width, height = 400, 400
path = "/home/umi/Pictures/ed.jpeg"
img = cv2.imread(path)
print(img.shape)
resized_img = cv2.resize(img, (width, height))
print(img.shape)

imgCropped = img[200:600, 401:800]







# cv2.imshow("laraib", resized_img)
cv2.imshow("laraib Cropped", imgCropped)
cv2.waitKey(0)