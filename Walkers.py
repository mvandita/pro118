import cv2


# Create our body classifier
body_classifier =cv2.CascadeClassifier('haarcascade_fullbody.xlm')


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray,1.2,3)
    
    
    # Extract bounding boxes for any bodies identified
    success, bbox = tracker.update(img)
    
    cv2.imshow("result", img)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
