import sys, os
from glob import glob
import re
from itertools import islice

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

file_list = glob("/Users/matina/Desktop/New_str_mat_xyz/ChemSci/*")
all_files = []
for file in os.listdir("/Users/matina/Desktop/New_str_mat_xyz/ChemSci"):
    if file.endswith(".xyz"):
        all_files.append(os.path.join("/Users/matina/Desktop/New_str_mat_xyz/ChemSci", file))
all_files.sort(key=natural_keys)
count=0
for k in range(len(all_files)):
    with open(all_files[k]) as infile:
#with open("/Users/matina/Desktop/newc_62.xyz") as infile:
        p=infile.name.split('/')
        print(p)
#        t=p[5].split('_')
        m=p[6].split('.')
        print (m[0])
        file = open("/Users/matina/Desktop/New_str_mat_xyz/ChemSci/a_%s.inp" % m[0], "w+")
#        file = open("/Users/matina/Desktop/input_62.inp", "w+")
        file.write("! PBE def2-SVP D3BJ RI AutoAux xyzfile Opt PAL4 \n")
        file.write("\n")
        file.write("%base"+"\"gas%s\"\n" % m[0])
        file.write("\n")
        file.write("%maxcore 4000\n")
        file.write("\n")
        file.write("*xyz -1 1\n")
        for line in islice(infile,2,None):
            pass
            file.write(line)
#        for line in infile:
#            file.write(line)
        file.write("*\n")
        file.write("\n")
        
        file.write("$new_job\n")
        file.write("! PBE def2-SVP D3BJ RI AutoAux CPCM Opt\n")
        file.write("%base"+"\"solvent%s\"\n" % m[0])
    
        file.write("\n")
        file.write("%CPCM\n")
        file.write("SMD true\n")
        file.write("SMDsolvent \"dichloromethane\"\n")
        file.write("end\n")
        file.write("*xyzfile -1 1\n")
        file.write("\n")

