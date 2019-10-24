import cv2
import numpy as np

cap=cv2.VideoCapture(1)

forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while True:
    rev,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow(frame)
    cv2.imshow(gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()



# cv2.line can be used to draw a line on the image
# cv2.rectangle, cv2.circle, cv2.polylines ,cv2.putText is for adding text on 
# the image..