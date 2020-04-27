#!/usr/bin/python
from __future__ import print_function, absolute_import

import subprocess, sys, os
from os import listdir
from os.path import isfile, join
import datetime
from glob import glob
import re
from sterimoltools import *
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

    file_list = glob("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt/atoms")
    all_files = []
    for file in os.listdir("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt/atoms"):
        if file.endswith(".txt"):
            all_files.append(os.path.join("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt/atoms", file))
    all_files.sort(key=natural_keys)

    file_list1 = glob("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt")
    all_files1 = []
    for file1 in os.listdir("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt"):
        if file1.endswith(".pdb"):
            all_files1.append(os.path.join("/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt", file1))
    all_files1.sort(key=natural_keys)
    T2=[]

    for k in range(len(all_files)):
    
        p=all_files[k].split('/')
        p1=all_files1[k].split('/')
        numb1=p1[10]
        print (p1[10])
        numb=p[11]
        print (p[11])
        
        id1,id2 = idfile2ids(all_files[k])
        print(id1,id2)
        T2 = Sterimol(id1,id2,numb1,"/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt/%s" %numb1,"False")
        print(T2)
        df = pandas.DataFrame(T2)
        df.to_csv('/Users/matina/Desktop/modifications/scaffolds/scaffoldsopted/Modifications3-3/optimisedModifications/SatEt/SatEt3-3Sterimol.csv',sep=",", float_format='%.2f',line_terminator='\n',encoding='utf-8')
        del id1[:]
        del id2[:]
