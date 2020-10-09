#!/usr/bin/python
from __future__ import print_function, absolute_import

import subprocess, sys, os
from os import listdir
from os.path import isfile, join
import datetime
from glob import glob
import re
from sterimoltools2Toms import *
import pandas
import csv
########################################
########### S T E R I M O L ############
########################################
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
        alist.sort(key=natural_keys) sorts in human order
        '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def idfile2ids(id_filename):
    
    id1,id2 = [],[]

    for line in open(id_filename, 'r'):
        id1.append(line.split()[0])
        id2.append(line.split()[1])
    return id1,id2


def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", action='store', help='.inp file(s) sumbit to the queue', nargs='+')
    
    return parser.parse_args()

def Sterimol(atomid1, atomid2, n,directory , verbose = "False"):
                    
                    total = []
                    print("I am here")
                    for i in range (len(atomid1)):
                            print(directory)
                            file_Params = calcSterimol(directory, "bondi", int(atomid1[i]), int(atomid2[i]), verbose)
                            print("NOW I am here")
                            lval = file_Params.lval; B1 = file_Params.B1; B5 = file_Params.newB5
                            total.append(n)
                            total.append(lval)
                            total.append(B1)
                            total.append(B5)
                    T2.append(total)
                    
                    return T2
if __name__ == '__main__':

#   the number of documents should be the same in both files
#   one file contains documents with the ids of the pairs we want to calculate sterimol parameters for
#   the other files should contain the pdb files of the molecules we want to calulate sterimol parameters for

    file_list = glob("/mnt/d/Sterimol/Examples/Model5/atoms/*")
    all_files = []
    for file in os.listdir("/mnt/d/Sterimol/Examples/Model5/atoms"):
        if file.endswith(".txt"):
            all_files.append(os.path.join("/mnt/d/Sterimol/Examples/Model5/atoms", file))
    all_files.sort(key=natural_keys)

    file_list1 = glob("/mnt/d/Sterimol/Examples/Model5/*")
    all_files1 = []
    for file1 in os.listdir("/mnt/d/Sterimol/Examples/Model5"):
        if file1.endswith(".pdb"):
            all_files1.append(os.path.join("/mnt/d/Sterimol/Examples/Model5", file1))
    all_files1.sort(key=natural_keys)
    T2=[]

    for k in range(56,len(all_files)):
    
        p=all_files[k].split('/')
        p1=all_files1[k].split('/')
        numb1=p1[6]
        print (p1[6])
        numb=p[6]
        print (p[6])
        
        id1,id2 = idfile2ids(all_files[k])
        print(id1,id2)
        T2 = Sterimol(id1,id2,numb1,"/mnt/d/Sterimol/Examples/Model5/%s" %numb1,"False")
        print(T2)
        df = pandas.DataFrame(T2)
        df.to_csv('/mnt/d/Sterimol/Model5.csv',sep=",", float_format='%.2f',line_terminator='\n',encoding='utf-8')
        del id1[:]
        del id2[:]
