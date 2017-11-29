

import cv2
import numpy as np
import time


ImgPath = '/home/wmh/work/seqbuff/usb-cam'
ni = 0
CamON = False

cap = cv2.VideoCapture(0)
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
    if cv2.waitKey(50) & 0xFF == ord(' '):
        CamON = not CamON
        print "Camera:", CamON
    if CamON:
        cv2.imwrite(ImgPath+'/'+"%s.jpg" % ni,frame)
        print 'Save image:', ImgPath+'/'+"%s.jpg" % ni
        ni += 1

cap.release()
cv2.destroyAllWindows()

