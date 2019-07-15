#!/usr/bin/env python3

import os
import re
from codecs import open
import numpy
import math

all_files = []
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
for file in os.listdir("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/SPoutputs/2b-Mono"):
     if file.endswith(".out"):
         # print(os.path.join("/Users/matina/Desktop/xtbout/", file))
         all_files.append(os.path.join("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/SPoutputs/2b-Mono", file))
all_files.sort(key=natural_keys)
# print (all_files)

def get_e(out_filename):

    e = 0
    # if infile.endswith('.out'):
    for line in open(out_filename, 'r',encoding="utf-8", errors="ignore"):
            if 'FINAL SINGLE POINT ENERGY' in line:
                e = float(line.split()[4])

    if not all([e]) != 0:
        print('Error in extracting thermochemical data from \t', infile)

    return [e]


if __name__ == '__main__':

    e,name,normalized_e,expo,J,Σ,w = [],[],[],[],[],[],[]
    Σex,Σw,count = 0,0,0

    K=300 # in kelvin
    R=8.3144598 #gas constant J/K/mol
    RK=R*K

    for k in range(len(all_files)):
        name.append(all_files[k].split('/')[9])
        with open(all_files[k]) as infile:
                for line in infile:
                    if 'FINAL SINGLE POINT ENERGY' in line:
                        e.append (float(line.split()[4]))
    normalized_e=[]
    # name =['zero', 'zero81']
    # e = [-2033898.381 , -2033901.9 ]
    name = numpy.array(name)
    e = numpy.array(e)
    inds = e.argsort()
    sorted_name = name[inds]
    sorted_e = e[inds]
    print(sorted_name,sorted_e)
    print(len(e))
    for i in range (len(sorted_e)):
        normalized_e.append(round(sorted_e[i]-sorted_e[0],11))

    print(normalized_e)
    for i in range(len(normalized_e)):
        J.append(round(normalized_e[i]*(2625.50*1000),11))
    print(J)

    for i in range(len(J)):
        expo.append(round(math.exp(-(J[i]/RK)),11))
    print(expo)
    Σex = round(sum(expo),11)
    print(Σex)

    for i in range (len(expo)):
        # print(expo[i],Σex)

        w.append(round(expo[i]/Σex,11))
    print(w)

    for i in range(len(w)):
        Σw = Σw + w[i]
        print(Σw)
        count = count +1
        if Σw > 0.90:
            break
    print(count)

    with open('/Users/matina/Desktop/New_str_mat_xyz/XTB/J/SPoutputs/2b-Mono/2b-Mono.csv', 'a') sv_fas cile:
        for i in range (count):
            print (sorted_name[i],file = csv_file)
