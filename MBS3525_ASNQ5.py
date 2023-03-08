import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('Trackbar')
cv2.createTrackbar('x','Trackbar',0,640,nil)
cv2.createTrackbar('y','Trackbar',0,480,nil)

while True:
    success, frame = cam.read()

    x = cv2.getTrackbarPos('x','Trackbar')
    y = cv2.getTrackbarPos('y', 'Trackbar')
    # cv2.rectangle(frame, (x,y),(x+100,y+100),(255,0,0),5)
    frame = cv2.line(frame, (x,0), (x, 480), (255, 0, 0), 5)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xff == 27: # 27 = ESCAPE
        break

cam.release()
cv2.destroyAllWindows()