import cv2
# frame =f1
# roi_color =f2
# gray = Grey
# f2=f1
# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('C:/Users/cr123/PycharmProjects/pythonProject1/Resources/haarcascade_frontalface_default.xml')
font=cv2.FONT_HERSHEY_SIMPLEX
# Start the video capture from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a bounding rectangle around each face and display it in color
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        temp=frame[y:y+h, x:x+w]
        frame=gray
        frame=cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        frame[y:y+h, x:x+w]=temp
        cv2.putText(frame, 'MBS3523 Assignment 1-Q4  Name: Tang Long Him', (20, 50), font, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Stop the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
