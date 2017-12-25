# some IMU ultity
import numpy as np
from matplotlib import pylab
from mpl_toolkits import mplot3d

def loadcsv(CSVFILE):
    dataset = []
    # scale = 1
    for line in open(CSVFILE).readlines():
        data = line.split(",")
        if data[0][0].isdigit():
            dataset.append([float(x) for x in data])
    return dataset

# Rawdata is a numpy array, raw ACC output
def GravityFilter(Rawdata, g0 = np.array([0.0,0.0,0.0])):
    alpha = 0.8  # In Android SDK, alpha = 0.8
    # g = np.array([0.0,0.0,0.0])

    g = alpha*g0 + (1-alpha)*Rawdata
    Acc = Rawdata - g
    return  g,Acc
    pass

def main():
    CSVFILE = '/media/wmh/TEMP/SlamTestSeq/MySeq/Still1/RobotState.csv'
    dataset = loadcsv(CSVFILE)
    ColStart = 10
    ColEnd = 12
    gravity = np.array([0.0,0.0,0.0])
    AccSum = np.array([0.0,0.0,0.0])
    GNormArray =[]


    for data in dataset:
        gravity,acc = GravityFilter(np.array(data[ColStart:ColEnd+1]),gravity)
        AccSum += acc
        GNormArray.append(np.linalg.norm(gravity))
        print "g:",gravity,":",np.linalg.norm(gravity),"; Acc:",acc

    GNormArray = np.array(GNormArray)
    print np.std(GNormArray)
    print "Sum of Acc:", AccSum
    pass


if __name__ == '__main__':
    main()