import os
from glob import glob
import re

#p = 0
#p = int(p)
#all_files = []
#def atoi(text):
#    return int(text) if text.isdigit() else text
#
#def natural_keys(text):
#    '''
#    alist.sort(key=natural_keys) sorts in human order
#    http://nedbatchelder.com/blog/200712/human_sorting.html
#    '''
#    return [ atoi(c) for c in re.split('(\d+)', text) ]
#for file in os.listdir("/Users/matina/Desktop/1urea_pdbs/"):
#     if file.endswith(".pdb"):
#         print(os.path.join("/Users/matina/Desktop/1urea_pdbs/", file))
#         all_files.append(os.path.join("/Users/matina/Desktop/1urea_pdbs/", file))
#all_files.sort(key=natural_keys)
#print (all_files)
#
#for k in range(len(all_files)):
#     with open(all_files[k]) as infile2:
#         p=infile2.name.split('_')
#         print (p[2])
#    with open('/Users/matina/Desktop/1urea_F_pdbs/newc_f_%s' %(p[2]), 'w',encoding="utf8", errors='ignore') as outfile:
with open('/Users/matina/Desktop/new_c62.pdb', 'r',encoding="utf8", errors='ignore') as infile2:
    with open('/Users/matina/Desktop/newc_f_62.pdb', 'w',encoding="utf8", errors='ignore') as outfile:
                     if infile2:
                         current_line = infile2.readline()
                         outfile.write(current_line)

                     for line in infile2:
                         previous_line = current_line
                         current_line = line
                         p_l = previous_line.split()
                         c_l = current_line.split()

                         if c_l[0] == 'HETATM':
                             outfile.write(current_line)
                             j=int(c_l[1])

                         if c_l[0] == 'CONECT' and p_l[0] == 'HETATM':
                             print("edw")
                             j = j + 1
                             if j>=100:
                                 j = str(j)
                                 outfile.write("HETATM" + '  ' + j + '  ' + "F" + '   ' + "UNL" + '     ' + "1" + '      ' + "-1.021" + '   ' + "1.696 " + '  ' + "1.048 " + ' ' + "1.00" + '  ' + "0.00" + '           ' + "F\n")
                             elif j<100:
                                 j = str(j)
                                 outfile.write("HETATM" + '   ' + j + '  ' + "F" + '   ' + "UNL" + '     ' + "1" + '      ' + "-1.021" + '   ' + "1.696 " + '  ' + "1.048 " + ' ' + "1.00" + '  ' + "0.00" + '           ' + "F\n")
                         if c_l[0] == 'CONECT':
                             outfile.write(current_line)
                         if c_l[0] == 'END':
                             outfile.write(current_line)

     # p=p+1
