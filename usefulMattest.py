from __future__ import print_function
import sys
import numpy as np
import os
import pandas
from glob import glob
import re

all_files = []
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
for file in os.listdir("/Users/matina/Desktop/nucleophilicity/alcohol/s1e"):
     if file.endswith(".out"):
         print(os.path.join("/Users/matina/Desktop/nucleophilicity/alcohol/s1e", file))
         all_files.append(os.path.join("/Users/matina/Desktop/nucleophilicity/alcohol/s1e", file))
all_files.sort(key=natural_keys)
print (all_files)


filepath=[]
T1=[]
T2=[]
#directory = '/Users/matina/Desktop/everything_new/2urea_outputs/outputswithF'
#for file in os.listdir(directory):
#    filename = os.fsdecode(file)
#    if filename.endswith(".out"):
#        filepath.append(filename)

for k in range(len(all_files)):
 with open(all_files[k]) as infile:
    
    j=os.path.join(all_files[k])

    eV, M, H = [], [], []
    HN, Hid, Fids, HF, NC, Cid=[], [], [], [], [], []
    flag=0
    flag2=0
    totalHcharge=0
    totalNMRc=0
    totalNMRh=0
    total = []
    with open(j, 'r') as infile:
        for i, l in enumerate(infile):
            found = l.count('NO   OCC          E(Eh)            E(eV)')
            if found:
                where = i
    with open(j, 'r') as infile:
        for i2, l2 in enumerate(infile):
            found2 = l2.count('  Mayer bond orders larger than 0.1')
            if found2:
                where2 = i2
    with open(j, 'r') as infile:
         for i3, l3 in enumerate(infile):
             found3 = l3.count('  ATOM     CHARGE      SPIN')
             if found3:
                 where3 = i3
    with open(j, 'r') as infile:
        for i4, l4 in enumerate(infile):
            found4 = l4.count('Magnitude (Debye)')
            if found4:
                where4 = i4
    with open(j, 'r') as infile:
        for i5, l5 in enumerate(infile):
            found5 = l5.count('FINAL SINGLE POINT ENERGY')
            if found5:
                where5 = i5
    with open(j, 'r') as infile:
        for i6, l6 in enumerate(infile):
            found6 = l6.count(' ATOM       NA         ZA         QA         VA         BVA        FA')
            if found6:
                where6 = i6
    with open(j, 'r') as infile:
        for i7, l7 in enumerate(infile):
            found7 = l7.count('  Nucleus  Element    Isotropic     Anisotropy')
            if found7:
                where7 = i7

    with open(j, 'r') as infile:
        always_print = False
        lines = infile.readlines()

#    # HOMO-LUMO
#        for line in lines[where:]:
#            if always_print or "NO   OCC          E(Eh)            E(eV) " in line:
#                always_print = True
#                eV.append(line.split()[3])
#                if (line.split()[1]) == '0.0000':
#                    always_print = False
#        HOMO = (eV[-2])
#        total.append(HOMO)
#        LUMO = (eV[-1])
#        total.append(LUMO)
#        print("HOMO: %s eV" %HOMO)
#        print("LUMO: %s eV\n" %LUMO)

    #   id of THE F it will always be the one at the end
        for line in lines[where6:]:
            if always_print or "  ATOM       NA         ZA         QA         VA         BVA        FA" in line:
                always_print = True
                if (len(line.split())) > 0:
                    if line.split()[1]=='F':
                        Fids.append(int(line.split()[0]))
                if (len(line.split())) == 0:
                    always_print = False
        if len(Fids)>0:
            Fid=sorted(Fids, reverse=True)[0]
            flag2=1
    #    print(Fid)
    #    mayer bond orders
        for line in lines[where2:]:
            if always_print or "  Mayer bond orders larger than 0.1" in line:
                always_print = True
                split = line.split('B')
                l = len(split)
                for i in range(l):
                    if 'N' in split[i] and 'H' in split[i]:
                        HN.append(split[i])
                    if flag2 == 1:
                        if str(Fid) in split[i] and 'H' in split[i] and 'F' in split[i]:
                            HF.append(split[i])
                            flag=1
                    if 'N' in split[i] and 'C' in split[i]:
                        NC.append(split[i])
                if '------------------' in line:
                    always_print = False
    #    print(NC)
#        for i in range(len(HN)):
#            print("N-H Bond:", HN[i])
#            total.append(HN[i])
#            hn_split = HN[i].split(',')
#    #        print (hn_split[0])
#            if 'H' in hn_split[0]:
#                one = hn_split[0].strip()
#                one = one.split("-")
#                Hid.append(one[0].strip("( "))
#    #        print (hn_split[1])
#            if 'H' in hn_split[1]:
#                one = hn_split[1].strip()
#                one = one.split("-")
#                Hid.append(one[0].strip("( "))
    #    print(Hid)
#        for i in range(len(NC)):
#            print("N-C Bond:", NC[i])
#            total.append(NC[i])
#            nc_split = NC[i].split(',')
#            if 'C' in nc_split[0]:
#                one = nc_split[0].strip()
#                one = one.split("-")
#                Cid.append(one[0].strip("( "))
#            if 'C' in nc_split[1]:
#                one = nc_split[1].strip()
#                one = one.split("-")
#                Cid.append(one[0].strip("( "))
        for i in range(len(HF)):
            print("F-H Bond:", HF[i])
            total.append(HF[i])
            hf_split = HF[i].split(',')
            if 'H' in hf_split[0]:
                one = hf_split[0].strip()
                one = one.split("-")
                Hid.append(one[0].strip("( "))
            if 'H' in hf_split[1]:
                one = hf_split[1].strip()
                one = one.split("-")
                Hid.append(one[0].strip("( "))
#    #    print(Cid)
#    #    print(Hid)
        Hids=list(set(Hid))
#        Cids=list(set(Cid))
    #    print (Cids)
    #    print (Hids)
    #     Hirshfeld
        for line in lines[where3:]:
            if always_print or "  ATOM     CHARGE      SPIN" in line:
                always_print = True
                if (len(line.split())) > 0:
#                    for j in range(len(Hids)):
#                        if line.split()[0] == Hids[j]:
#                            print("H%s atomic charge: %s e" % (line.split()[0], line.split()[2]))
#                            totalHcharge=totalHcharge+float(line.split()[2])
#                            total.append(line.split()[0]+"H "+line.split()[2])
                    if flag2 == 1:
                        if line.split()[0] == str(Fid) and flag == 1:
                            print("F%s atomic charge: %s e" % (line.split()[0], line.split()[2]))
                            total.append(line.split()[0]+"F "+line.split()[2])
#                    if line.split()[0] == 'TOTAL':
#                        print("Total charge: %s e" % line.split()[1])
#                        total.append(line.split()[1])
                if '-------' in line:
                    always_print = False
#        avHcharge=totalHcharge/len(Hids)
#        total.append(avHcharge)
#        print ("avarege H charges:",avHcharge)
#    #   Dipole
#        for line in lines[where4:]:
#            if 'Magnitude (Debye)' in line:
#                dipole = float(line.split()[3])
#                print("DIPOLE MOMENT : Magnitude (Debye)      :      %f\n" %dipole)
#                total.append(dipole)
#    #   FINAL SINGLE POINT ENERGY
#        for line in lines[where5:]:
#            if 'FINAL SINGLE POINT ENERGY' in line:
#                e = float(line.split()[4])
#                print("FINAL SINGLE POINT ENERGY:      %f HARTREE\n" %e)
#                total.append(e)

    #   NMR shifts
#        for line in lines[where3:]:
#            if always_print or "  Nucleus  Element    Isotropic     Anisotropy" in line:
#                always_print = True
#                if (len(line.split())) > 0:
#                    for j in range(len(Hids)):
#                        if line.split()[0] == Hids[j]:
#                            print("H%s NMR shift: %s ppm" % (line.split()[0], line.split()[2]))
#                            totalNMRh = totalNMRh+float(line.split()[2])
#                            total.append(line.split()[0]+line.split()[2])
#                    for j in range(len(Cids)):
#                        if line.split()[0] == Cids[j]:
#                            print("C%s NMR shift: %s ppm" % (line.split()[0], line.split()[2]))
#                            totalNMRc = totalNMRc+float(line.split()[2])
#                            total.append(line.split()[0]+line.split()[2])
#                    if flag2 == 1:
#                        if line.split()[0] == str(Fid) and flag == 1:
#                            print("F%s NMR shift: %s ppm" % (line.split()[0], line.split()[2]))
#                            total.append(line.split()[2])
#        avNMRh=totalNMRh/len(Hids)
#        print("avarege H NMRshifts :",avNMRh)
#        total.append(avNMRh)
#        avNMRc=totalNMRc/len(Cids)
#        print ("avarege C NMRshifts :",avNMRc)
#        total.append(avNMRc)
    T2.append(total)
    df = pandas.DataFrame(T2)
    df.to_csv('/Users/matina/Desktop/alcoholF_out.csv')
