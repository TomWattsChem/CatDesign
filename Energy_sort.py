# This script extracts the energies after ORCA optimization and returns a csv file with the energies sorted.

import os
import re
from codecs import open
import numpy
import math


all_files = []
e, name = [], []

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
for file in os.listdir("/Users/matina/Desktop/Conf-Opt/1urea/c77/"):
     if file.endswith(".out"):
         print(os.path.join("/Users/matina/Desktop/Conf-Opt/1urea/c77/", file))
         all_files.append(os.path.join("/Users/matina/Desktop/Conf-Opt/1urea/c77/", file))

all_files.sort(key=natural_keys)
print (all_files)
# outputfile = open("finalenergies.csv", "w").close()

for k in range(len(all_files)):
    name.append(all_files[k].split('/')[7])
    with open(all_files[k]) as infile:
        j = os.path.join(all_files[k])

        with open(j, 'r') as infile:
            for i, l in enumerate(infile):
                found = l.count('FINAL SINGLE POINT ENERGY')
                if found:
                    where = i
        with open(j, 'r') as infile:
            always_print = False
            lines = infile.readlines()

            for line in lines[where:]:
                if 'FINAL SINGLE POINT ENERGY' in line:
                    e.append(float(line.split()[4]))
                    # print("FINAL SINGLE POINT ENERGY:      %f HARTREE\n" % e)

name = numpy.array(name)
e = numpy.array(e)
inds = e.argsort()
sorted_name = name[inds]
sorted_e = e[inds]
print(sorted_name,sorted_e)
with open ("/Users/matina/Desktop/Conf-Opt/1urea/c77/finalenergies.csv", "a") as outputfile:
    for i in range(len(sorted_e)):
        print(sorted_name[i],sorted_e[i], file=outputfile)