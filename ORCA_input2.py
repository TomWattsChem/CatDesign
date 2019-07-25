import sys, os
from glob import glob
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

file_list = glob("/Users/matina/Desktop/new*")
all_files = []
for file in os.listdir("/Users/matina/Desktop/new/"):
    if file.endswith(".xyz"):
        all_files.append(os.path.join("/Users/matina/Desktop/new/", file))
all_files.sort(key=natural_keys)
count=0
for k in range(len(all_files)):
    with open(all_files[k]) as infile:
#with open("/Users/matina/Desktop/newc_62.xyz") as infile:
        p=infile.name.split('/')
        print(p)
        t=p[5].split('_')
        m=t[1].split('.')
        print (m[0])
        file = open("/Users/matina/Desktop/new/new_%s_job3.inp" % m[0], "w+")
#        file = open("/Users/matina/Desktop/input_62_job3.inp", "w+")

        file.write("! PBE def2-TZVP D3BJ RI AutoAux NMR CPCM PAL4 \n")
        file.write("%base"+"\"solvent%s_1\"\n" % m[0])
        file.write("%maxcore 4000\n")
        
        file.write("\n")
        file.write("%CPCM\n")
        file.write("SMD true\n")
        file.write("SMDsolvent \"dichloromethane\"\n")
        file.write("end\n")
        file.write("\n")
        file.write("%output\n")
        file.write("Print[P_Hirshfeld] 1\n")
        file.write("end\n")
        file.write("*xyzfile - 1 1 /u/fd/orie3990/ORCA/new/solvent%s.xyz\n" % m[0])
        file.write("% eprnmr\n")
        file.write("Nuclei = all H {shift}\n")
        file.write("Nuclei = all C {shift}\n")
        file.write("Nuclei = all F {shift}\n")
        file.write("end\n")

#        count = count + 1
