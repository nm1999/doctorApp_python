import cv2
from cv2 import threshold
from cv2 import dilate
from matplotlib.pyplot import contour
from numpy import diff
cap = cv2.VideoCapture(0)

def get_video():
    while True:
        ret,frame1 = cap.read()
        ret,frame2 = cap.read()
        diff = cv2.absdiff(frame1,frame2)
        gray= cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thres = cv2.threshold(blur,20,255,0,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thres,None,iterations=3)
        contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame1,contours,-1,(0,225,0),2)

        cv2.imshow("frame",frame1)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()