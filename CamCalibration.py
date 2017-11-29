import numpy as np
import cv2
import glob

print("Start camera processing...")
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

ImgPath = '/home/wmh/work/seqbuff/'
# images = glob.glob('*.png')
images = glob.glob(ImgPath + '*.jpg')
images = images + glob.glob(ImgPath + '*.png')


# print (len(images)," images are found.")

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # gray = img

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
    # cv2.imwrite('g'+fname,gray)
    print fname,": ",ret

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7, 6), corners, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
        cv2.destroyAllWindows()

print "Find: ", len(objpoints)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print "Cam Matrix: ", mtx
print "fx =",mtx[0,0]
print "fy =",mtx[1,1]
print "cx =",mtx[0,2]
print "cy =",mtx[1,2]

print "Distortion Factor: ", dist
dist = dist.reshape(5,1)
print "k1 =",dist[0]
print "k2 =",dist[1]
print "p1 =",dist[2]
print "p2 =",dist[3]
print "k3 =",dist[4]