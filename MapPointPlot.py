import numpy as np
import random
from matplotlib import pylab
from mpl_toolkits import mplot3d
from itertools import combinations
# import matplotlib.pyplot as plt

def plot_plane(a, b, c, d,size =2):
	xx, yy = np.mgrid[-1*size:size, -1*size:size]
	return xx, yy, (-d - a * xx - b * yy) / c

# To load Map Points, in csv format
def loadcsv(TRACE_FILE):
    points = []
    # scale = 1
    for line in open(TRACE_FILE).readlines():

    	data = line.split(",")
    	if not 'Id' in data[0]:
    		# print data[0]
    		points.append([float(data[6]), float(data[7]), float(data[8])])

    print "Got", len(points), "points"
    return np.array(points)


def main():
    fig = pylab.figure()
    ax = mplot3d.Axes3D(fig)
    TRACE_FILE = '/home/wmh/work/ORB_SLAM2_wmh-ubuntu/Examples/Monocular/MapInfo/MPInfo_2125.csv'
    xyzs = loadcsv(TRACE_FILE)
    ax.scatter3D(xyzs.T[0], xyzs.T[1], xyzs.T[2])

    # xx, yy, zz = plot_plane(a, b, c, d)
    xx, yy, zz = plot_plane(0, 1, 0, 0)   #XOZ Plane
    ax.plot_surface(xx, yy, zz, color=(0, 1, 0, 0.5))

    pylab.show()


if __name__ == '__main__':
	main()