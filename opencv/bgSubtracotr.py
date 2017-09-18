#!python3
import numpy as np
import cv2
import sys
import time

if len(sys.argv) == 1:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(sys.argv[1])

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    fgmask = cv2.medianBlur(fgmask, 7)
    cv2.imshow('frame', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
