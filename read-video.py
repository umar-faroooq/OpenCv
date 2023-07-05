import cv2
frameWidth = 480
frameHeight = 360

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)



while True:
    succes, img = cap.read()
    cv2.imshow("video", img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


