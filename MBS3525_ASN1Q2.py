import cv2
print(cv2.__version__)
webcam = cv2.VideoCapture(0)
# webcam2 = cv2.VideoCapture(1)
while True:
    ret,frame = webcam.read()
    print(frame.shape)
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    (thresh, bwFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)
    # ret2, image2 = webcam2.read()
    cv2.imshow('Normal',frame)
    cv2.imshow("Black and White",bwFrame)
    # cv2.imshow('Window 2', image2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
webcam.release()
# webcam2.release()
cv2.destroyAllWindows()
