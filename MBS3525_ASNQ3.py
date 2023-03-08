import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('Trackbar')
cv2.createTrackbar('x','Trackbar',100,640,nil)
cv2.createTrackbar('y','Trackbar',100,480,nil)
x, y = 0, 0
cx, cy = 4,4

while True:
    success, frame = cam.read()
    print(frame.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX
    x += cx
    y += cy
    if x < 0:
        x = 0
        vx = -vx
    elif x + 80 > frame.shape[1]:
        x = frame.shape[1] -80
        cx = -cx
    if y < 0:
        y = 0
        cy = -cy
    elif y +80 > frame.shape[0]:
        y = frame.shape[0] - 80
        cy = -cy

    # x = cv2.getTrackbarPos('x','Trackbar')
    # y = cv2.getTrackbarPos('y', 'Trackbar')
    # cv2.rectangle(frame, (x,y),(x+100,y+100),(255,0,0),5)
    cv2.rectangle(frame, (x,y), (x+80,y+80), (0, 255, 0), 3)
    cv2.putText(frame, 'MBS3523 Assignment 1-Q4  Name: Tang Long Him', (20, 50), font,
                0.5, (0, 255, 0), 2)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xff == 27: # 27 = ESCAPE
        break

cam.release()
cv2.destroyAllWindows()