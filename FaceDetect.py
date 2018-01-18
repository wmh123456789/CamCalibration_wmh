import cv2

ImgPath = '/media/wmh/TEMP/SlamTestSeq/MySeq/CarMove2/'
StartNo = 1
EndNo = 2480

for i in xrange(StartNo,EndNo):
    img = cv2.imread(ImgPath+str(i)+'.jpg',0)
    # print ImgPath+str(i)+'.jpg'
    cv2.imshow('Car Cam',img)
