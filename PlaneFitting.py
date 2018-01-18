import numpy as np
import random
from matplotlib import pylab
from mpl_toolkits import mplot3d
from itertools import combinations
# import matplotlib.pyplot as plt


def run_ransac(data, estimate, sample_size, goal_inliers, max_iterations,Inlier_margin = 2, stop_at_goal=True, random_seed=None):
	best_ic = 0
	best_model = None
	random.seed(random_seed)
	for i in xrange(max_iterations):
		s = random.sample(data, int(sample_size))
		m = estimate(s)
		ic = 0
		for j in xrange(len(data)):
			if is_inlier(m, data[j],threshold=Inlier_margin):
				ic += 1

		print s
		print 'estimate:', m,
		print '# inliers:', ic

		if ic > best_ic:
			best_ic = ic
			best_model = m
			if ic > goal_inliers and stop_at_goal:
				break
	print 'took iterations:', i+1, 'best model:', best_model, 'explains:', best_ic, " in ", len(data)
	return best_model, best_ic

def augment(xyzs):
	axyz = np.ones((len(xyzs), 4))
	axyz[:, :3] = xyzs
	return axyz

def estimate(xyzs):
	axyz = augment(xyzs[:3])
	return np.linalg.svd(axyz)[-1][-1, :]

def is_inlier(coeffs, xyz, threshold = 0.002):

	return np.abs(coeffs.dot(augment([xyz]).T)) < threshold

# Solve the distance between 2 3D points
def dist_PointToPoint(xyz1,xyz2):
	return np.linalg.norm(xyz1 - xyz2)
	# return np.sqrt(np.dot(xyz1-xyz2,xyz1-xyz2))

# Solve the distance of a 3D point to a plane
def dist_PointToPlane(xyz,abcd):
	m = np.sqrt(np.dot(abcd[:3], abcd[:3]))
	return np.dot(xyz,abcd[:3])/m

# Solve the projection of a 3D point to a plane
def proj_PointToPlane(xyz,abcd):
	m = np.sqrt(np.dot(abcd[:3],abcd[:3]))
	k = -1*dist_PointToPlane(xyz,abcd)/m
	return xyz + abcd[:3]*k

def plot_plane(a, b, c, d,size =1):
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
	return  np.array(points)

#  To load Cam center, in txt format
def loadtxt(TRACE_FILE):
	points = []
	fp = open(TRACE_FILE)
	for line in fp.readlines():
		data = line.split()
		# print data[0]
		points.append([float(data[1]), float(data[2]), float(data[3])])

	print "Got", len(points), "points"
	return np.array(points)



def main():
	fig = pylab.figure()
	ax = mplot3d.Axes3D(fig)

	# n = 10
	# max_iterations = 100
	# goal_inliers = n * 0.3

	# test data
	# xyzs = np.random.random((n, 3)) * 10
	# xyzs[:50, 2:] = xyzs[:50, :1]

	# Load data
	# TRACE_FILE = '/home/wmh/work/seqbuff/AroundDesk2/KeyFrameTrajectory.txt'
	# TRACE_FILE = '/home/wmh/work/seqbuff/OnDesk2/KeyFrameTrajectory.txt'
	# TRACE_FILE = '/home/wmh/work/ORB_SLAM2_wmh-ubuntu/Examples/Monocular/KeyFrameTrajectory.txt'
	TRACE_FILE = '/home/wmh/work/ORB_SLAM2_wmh-ubuntu/Examples/Monocular/MapInfo/MPInfo_2125.csv'

	xyzs = loadcsv(TRACE_FILE)
	# xyzs = loadtxt(TRACE_FILE)

	# xyzs = xyzs * 100

	n = xyzs.size/3
	max_iterations = 300
	goal_inliers = n * 0.8



	# RANSAC
	Inlier_margin = 0.01
	m, b = run_ransac(xyzs, estimate, 3, goal_inliers, max_iterations,Inlier_margin)
	# print "Model check(shuold be 1):",np.linalg.norm(m[:3])
	a, b, c, d = m
	xx, yy, zz = plot_plane(a, b, c, d)
	ax.plot_surface(xx, yy, zz, color=(0, 1, 0, 0.5))

	proj_points = []
	for point in xyzs:
		proj_points.append(proj_PointToPlane(point,m))

	ax.scatter3D(xyzs.T[0], xyzs.T[1], xyzs.T[2])
	# ax.scatter3D(proj_points.T[0], proj_points.T[1], proj_points.T[2])

# Test the MapPoints-Realworld Ratio
	dist = 0
	for p1,p2 in list(combinations(proj_points, 2)):
		d = dist_PointToPoint(p1,p2)
		if d > dist:
			dist = d
	print "The Max dist is:",dist

	pylab.show()


if __name__ == '__main__':
	main()
