import cv2
import numpy as np


kernel = np.ones((5,5), np.uint8)
print(kernel)


path = "/home/umi/Pictures/ed.jpeg"
img = cv2.imread(path)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2. GaussianBlur(imgGray, (5,5), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)

imgDilation = cv2.dilate(imgCanny, kernel, iterations =1)

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("laraib", img)
# cv2.imshow("laraib_gray", imgGray)
# cv2.imshow("Laraib Blurr", imgBlur)
# cv2.imshow("Laraib CAnny", imgCanny)
cv2.imshow("Laraib Dilation", imgDilation)
cv2.imshow("Laraib Erosion", imgEroded)
cv2.waitKey(0)