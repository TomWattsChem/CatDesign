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
os.makedirs("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/4",exist_ok=True)
file_list = glob("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/4/*.xyz")
all_files = []
for file in os.listdir("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/4"):
    if file.endswith(".xyz"):
        all_files.append(os.path.join("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/4", file))
all_files.sort(key=natural_keys)
count=0
for k in range(len(all_files)):
    with open(all_files[k]) as infile:
#with open("/Users/matina/Desktop/newc_62.xyz") as infile:
        p=infile.name.split('/')
        print(p)
        p=p[8].split('.')
        print (p[1])
        file = open("/Users/matina/Desktop/New_str_mat_xyz/XTB/J/4/input_%s.inp" % p[1], "w+")
#        file = open("/Users/matina/Desktop/input_62.inp", "w+")
        file.write("! PBE def2-SVP D3BJ RI AutoAux \n")
        file.write("\n")
        file.write("%base"+"\"gas%s\"\n" % p[1])
        file.write("\n")
#        file.write("%CPCM\n")
#        file.write("SMD true\n")
#        file.write("SMDsolvent \"dichloromethane\"\n")
#        file.write("end\n")
        file.write("%maxcore 4000\n")
        file.write("\n")
   
        file.write("*xyz -1 1\n")
        for line in islice(infile,2,None):
            pass
            file.write(line)
        file.write("*\n")
        file.write("\n")
        

