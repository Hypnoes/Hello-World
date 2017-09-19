import cv2
import time

#cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(r"C:\Users\Hypnoes\Desktop\vv\terrace1-c0.avi")
cap2 = cv2.VideoCapture(r"C:\Users\Hypnoes\Desktop\vv\terrace1-c2.avi")

#fast = cv2.FastFeatureDetector_create()
fgbg = cv2.createBackgroundSubtractorKNN()

orb = cv2.ORB_create()
sleep = 0
cont = 1

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    fgmask1 = fgbg.apply(frame1)
    fgmask2 = fgbg.apply(frame2)
    #old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #kp = fast.detect(gray, None)
    #kp = fast.detect(frame, None)
    fgmask1 = cv2.medianBlur(fgmask1, 7)
    fgmask2 = cv2.medianBlur(fgmask2, 7)
    fgmask1 = cv2.cvtColor(fgmask1, cv2.COLOR_GRAY2BGR)
    fgmask2 = cv2.cvtColor(fgmask2, cv2.COLOR_GRAY2BGR)
    det1 = cv2.bitwise_and(fgmask1, frame1)
    det2 = cv2.bitwise_and(fgmask2, frame2)
    if(ret1 == True and ret2 == True):
        kp1 = orb.detect(frame1, None)
        kp2 = orb.detect(frame2, None)
        kp1, des1 = orb.compute(det1, kp1)
        kp2, des2 = orb.compute(det2, kp2)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key= lambda x: x.distance)
        img3 = cv2.drawMatches(frame1, kp1, frame2, kp2, matches[:20], None, flags=2)
        #img3 = cv2.drawMatches(det1, kp1, det2, kp2, matches[:20], None, flags=2)
        cv2.imshow("video", img3)
        cv2.imwrite(f"out/cont_{cont}.png", img3)

    cont += 1
    if cv2.waitKey(1) & 0xff == ord('j'):
        sleep += 0.5
    if cv2.waitKey(1) & 0xff == ord('k'):
        if sleep <= 0:
            pass
        else:
            sleep -= 0.5
    print(f"Speed: {sleep}.", end='\r')
    time.sleep(sleep)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap1.release()
cap2.release()
