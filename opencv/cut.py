#!python3
# -*- coding:utf-8 -*-

import cv2
import sys
import time

cap = cv2.VideoCapture(sys.argv[1])

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

vw = cv2.VideoWriter(str(time.time()) + "_trans.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 30, size)
fgbg = cv2.createBackgroundSubtractorMOG2()


while True:
    success, frame = cap.read()
    
    if success:
        fgmask = fgbg.apply(frame)
        cv2.imshow("out", fgmask)
        transframe = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
        vw.write(transframe)
    else:
        break


cap.release()
vw.release()
cv2.destroyAllWindows()
