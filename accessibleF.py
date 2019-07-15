import os
import sys
from scipy.spatial import distance
import numpy as np
from glob import glob
import re
import shutil

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
        alist.sort(key=natural_keys) sorts in human order
        '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def exclude(xyzfile):
    
    coordinates,coordinatesMatrixf,coordinatesh,coordinatesMatrixh,coordinatesMatrix, distancesMatrix,distancesMatrixh,distancesMatrix1,coordinates1,coordinatesMatrix1 = [], [], [],[],[],[],[],[],[],[]
    xf,yf,zf,x,y,z,x1,y1,z1,xh,yh,zh = [],[],[],[],[],[],[],[],[],[],[],[]
    count,counth=0,0
    flag = 0
    flag1 = 0
    
    with open(xyzfile, "r") as file:
        lines = file.read().splitlines()
        last_line = lines[-1]           # the coordinates of the F
        xf.append(float(last_line.split()[1]))
        yf.append(float(last_line.split()[2]))
        zf.append(float(last_line.split()[3]))

        myArrayf=np.array((xf,yf,zf))
        myArrayf.astype(float)
        for i in range(len(xf)):
            af=myArrayf[0][i]
            bf=myArrayf[1][i]
            cf=myArrayf[2][i]
            coordinatesf=(af,bf,cf)
            coordinatesMatrixf.append(coordinatesf)
#        print(coordinatesMatrixf)
    with open(xyzfile, "r") as file:
        for line in file:
            if len(line.split()) == 4:
                if line.split()[0] == 'N':    # the coordinates of Ns

                    x.append(float(line.split()[1]))
                    y.append(float(line.split()[2]))
                    z.append(float(line.split()[3]))
    
                    myArray=np.array((x,y,z))
                    myArray.astype(float)
                elif line.split()[0] == 'H':    # the coordinates of Hs
                    
                    xh.append(float(line.split()[1]))
                    yh.append(float(line.split()[2]))
                    zh.append(float(line.split()[3]))
                    
                    myArrayh=np.array((xh,yh,zh))
                    myArrayh.astype(float)
                elif line.split() == last_line.split():  # not the last F
#                    print("found")
                    break
                else:                   # the coordinates of all other atoms
                    x1.append(float(line.split()[1]))
                    y1.append(float(line.split()[2]))
                    z1.append(float(line.split()[3]))

                    myArray1=np.array((x1,y1,z1))
                    myArray1.astype(float)

        for i in range(len(x)):
            a=myArray[0][i]
            b=myArray[1][i]
            c=myArray[2][i]
            coordinates=(a,b,c)
            coordinatesMatrix.append(coordinates)
#        print (coordinatesMatrix)
        for j in range (len(coordinatesMatrix)):            # distances between Ns and F
            dst = distance.euclidean(coordinatesMatrix[j], coordinatesMatrixf)
            distancesMatrix.append(dst)

        for i in range(len(xh)):
            ah=myArrayh[0][i]
            bh=myArrayh[1][i]
            ch=myArrayh[2][i]
            coordinatesh=(ah,bh,ch)
            coordinatesMatrixh.append(coordinatesh)
        #        print (coordinatesMatrix)
        for j in range (len(coordinatesMatrixh)):            # distances between Hs and F
            dsth = distance.euclidean(coordinatesMatrixh[j], coordinatesMatrixf)
            distancesMatrixh.append(dsth)

        for i in range(len(x1)):
            a1=myArray1[0][i]
            b1=myArray1[1][i]
            c1=myArray1[2][i]
            coordinates1=(a1,b1,c1)
            coordinatesMatrix1.append(coordinates1)
        #        print (coordinatesMatrix)
        for j in range (len(coordinatesMatrix1)):       # distances between all atoms and F
            dst1 = distance.euclidean(coordinatesMatrix1[j], coordinatesMatrixf)
            distancesMatrix1.append(dst1)

        for f in range (len(distancesMatrixh)):
            if distancesMatrixh[f] <= 2 :
                counth=counth+1
        if all(i > 2 for i in distancesMatrix1):
            flag=1
#            print("edw")
        print(distancesMatrix)
#        for f in range (len(distancesMatrix)):
#            if distancesMatrix[f] <= 3 :
##                print("gt??")
#                count=count+1
#        if count >= 2 and flag == 1 and counth >= 2:
        if flag == 1 and counth >= 2:
#                print ("lol")
                print(xyzfile)
                shutil.move("%s" %xyzfile,"/Users/matina/Desktop/unfittedXTB/unfitted/mat/c47/lessthan4/")


        del distancesMatrix[:]
        del distancesMatrix1[:]
        del distancesMatrixh[:]
        del x[:]
        del xf[:]
        del xh[:]
        del y[:]
        del yh[:]
        del yf[:]
        del z[:]
        del zh[:]
        del zf[:]
        count = 0


all_files=[]
if __name__ == '__main__':
    file_list = glob("/Users/matina/Desktop/unfittedXTB/unfitted/mat/c47/s.*.xyz")
    all_files = []
    for file in os.listdir("/Users/matina/Desktop/unfittedXTB/unfitted/mat/c47/"):
        if file.endswith(".xyz"):
            all_files.append(os.path.join("/Users/matina/Desktop/unfittedXTB/unfitted/mat/c47/", file))
    all_files.sort(key=natural_keys)
    os.makedirs("/Users/matina/Desktop/unfittedXTB/unfitted/mat/c47/lessthan4",exist_ok=True)
    for k in range(len(all_files)):
    
        p=all_files[k].split('.')
        p1=p[1].split('.')
        numb=p1[0]
        print (numb)
        exclude(all_files[k])
