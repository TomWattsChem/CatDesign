#!/usr/bin/python
from __future__ import print_function, absolute_import

import subprocess, sys, os
from os import listdir
from os.path import isfile, join
import datetime
from glob import glob
import re
from sterimoltools import *

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
#    i = 0

    for line in open(id_filename, 'r'):
#        i += 1
#        if len(line.split()) == 4 and i > 2:
        id1.append(line.split()[0])
        id2.append(line.split()[1])
    return id1,id2


def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", action='store', help='.inp file(s) sumbit to the queue', nargs='+')
    
    return parser.parse_args()

def Sterimol(atomid1, atomid2, n,directory , verbose = "False"):
    # If the directory exists
#    if os.path.exists(directory):

#        files = [f for f in listdir(directory) if isfile(join(directory, f)) and (f.split(".")[-1] == "pdb" or f.split(".")[-1] == "out") and len(f.split(".")) > 1 ]
                    print("I am here")
#        if len(files) > 0:

                    output = open("Sterimol_%s.txt" %n, 'w' )
                    message = " Structure                          L1 (A)   B1 (A)   B5 (A) \n"
                    output.write(message)
            
#                for filename in files:
#                    filesplit = filename.split(".")
                    #prepare the job
                    try:
                        for i in range (len(atomid1)):
                            file_Params = calcSterimol(directory, "bondi", int(atomid1[i]), int(atomid2[i]), verbose)
                            print("NOW I am here")
                            lval = file_Params.lval; B1 = file_Params.B1; B5 = file_Params.newB5
                            message = " %-31s " %n +" %8.2f" % lval+ " %8.2f" % B1+ " %8.2f" % B5
                            output.write("%s\n" % message)
                    except ValueError:
                        return False

#                    lval = file_Params.lval; B1 = file_Params.B1; B5 = file_Params.newB5
#                    message = " %-31s " % filename+" %8.2f" % lval+ " %8.2f" % B1+ " %8.2f" % B5
#                    output.write("%s\n" % message)
#                    output.close()

                    return True
#    else:
#        print("FATAL ERROR: Specified directory doesn't exist [%s]" % directory)
#        return False
if __name__ == '__main__':
    
    #    args = get_args()
    #    for filename in args.filenames:
    #
    #        xyzs = xyzfile2xyzs(filename)
    #        xyz_bonds(xyzs)
#   the number of documents should be the same in both files
#   one file contains documents with the ids of the pairs we want to calculate sterimol parameters for
#   the other files should contain the pdb files of the molecules we want to calulate sterimol parameters for

    file_list = glob("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/atoms/*")
    all_files = []
    for file in os.listdir("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/atoms"):
        if file.endswith(".txt"):
            all_files.append(os.path.join("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/atoms", file))
    all_files.sort(key=natural_keys)

    file_list1 = glob("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/*")
    all_files1 = []
    for file1 in os.listdir("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz"):
        if file1.endswith(".pdb"):
            all_files1.append(os.path.join("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz", file1))
    all_files1.sort(key=natural_keys)


    for k in range(len(all_files)):
    
        p=all_files[k].split('/')
        p1=all_files1[k].split('/')
        numb1=p1[8]
        print (p1[8])
#        p1=all_files1[k].split('c')
#        p=p[1].split('.')
        numb=p[9]
        print (p[9])
#    xyzs = xyzfile2xyzs(all_files[k])
#    xyz_bonds(xyzs,numb)

        id1,id2 = idfile2ids(all_files[k])
        print(id1,id2)
#        for i in range (len(id1)):
        Sterimol(id1,id2,numb1,"/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/%s" %numb1,"False")
        del id1[:]
        del id2[:]
