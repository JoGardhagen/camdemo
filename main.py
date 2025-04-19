import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Kunde inte öppen kameran")

print("Kameran är igång! Tryck ESC för att avsluta.")
time.sleep(3)

ret, ref_frame = cap.read()
ref_frame = cv2.resize(ref_frame,None,fx=0.5,fy=0.5)
ref_gray = cv2.cvtColor(ref_frame,cv2.COLOR_RGB2GRAY)

line_y = 350
threshold = 8000

print("Watching Line...")


while True:
    ret,frame = cap.read()
    if not ret:
        continue

    frame = cv2.resize(frame, None,fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    diff = cv2.absdiff(ref_gray,gray)
    _, thresh = cv2.threshold(diff,40,255,cv2.THRESH_BINARY)

    line_change = np.sum(thresh[line_y, :])

    if line_change > threshold:
        print("Goal Hit Line!")
        color = (0,0,255)
    else:
        color=(0,255,0)

    cv2.line(frame,(0,line_y),(frame.shape[1],line_y),color,2)

    cv2.imshow("Camera Line Watch",frame)
    cv2.imshow("Diff",thresh)
    
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()