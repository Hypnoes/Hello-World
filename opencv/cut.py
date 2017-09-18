#!python3
# -*- coding:utf-8 -*-

import cv2
import sys
import time

cap = cv2.VideoCapture(sys.argv[1])

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

vw = cv2.VideoWriter(str(time.time())[-6:] + "_trans.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 30, size)
#fgbg = cv2.createBackgroundSubtractorMOG2()


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret:
        #fgmask = fgbg.apply(frame)
        #cv2.imshow("out", fgmask)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vw.write(gray)
    else:
        break


cap.release()
vw.release()
cv2.destroyAllWindows()
