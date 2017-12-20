import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# TRACE_FILE = '/home/wmh/work/seqbuff/AroundDesk2/KeyFrameTrajectory.txt'
# TRACE_FILE = '/home/wmh/work/seqbuff/OnDesk2/KeyFrameTrajectory.txt'
TRACE_FILE = '/home/wmh/work/ORB_SLAM2_wmh-ubuntu/Examples/Monocular/KeyFrameTrajectory.txt'

x,y,z = [],[],[]
fp = open(TRACE_FILE)
for line in fp.readlines():
    data = line.split()
    # print data[0]
    x.append(float(data[1]))
    y.append(float(data[2]))
    z.append(float(data[3]))

# x,y,z = m[0],m[1],m[2]
ax=plt.subplot(111,projection='3d')


ax.scatter(x[:1000],y[:1000],z[:1000],c='y')
ax.scatter(x[1000:4000],y[1000:4000],z[1000:4000],c='r')
ax.scatter(x[4000:],y[4000:],z[4000:],c='g')

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()