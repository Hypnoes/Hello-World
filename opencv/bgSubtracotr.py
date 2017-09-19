#!python3
import numpy as np
import cv2
import sys
import os
import time

if len(sys.argv) == 1:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(sys.argv[1])

fgbg = cv2.createBackgroundSubtractorKNN()

fps = int(cap.get(cv2.CAP_PROP_FPS))
if fps >= 1:
    pass
else:
    fps = 30
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vw = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), fps, size)

cont = 1
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    fgmask = cv2.medianBlur(fgmask, 7)
    #fgmask = cv2.blur(fgmask, (2,2), fgmask)
    #gray = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', fgmask)
    
    if ret == True:
        #vw.write(fgmask)
        cv2.imwrite(f"out/out_{cont}.png", fgmask)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    cont += 1

cap.release()
cv2.destroyAllWindows()
