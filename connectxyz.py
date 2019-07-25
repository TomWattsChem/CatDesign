import numpy as np
import argparse
import sys, os
from glob import glob
import re

I,J=[],[]
I1,J1=[],[]
I2,J2=[],[]

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
        alist.sort(key=natural_keys) sorts in human order
        '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def xyz_bonds(xyzs, numb):
    """
        Determine the 'bonds' between
        :param xyzs:
        :param tolerance:
        :return:
        """
    tolerance=0.1
    for i in range(len(xyzs)):
        
        i_coords = np.array(xyzs[i][1:]).astype(float)
        
        for j in range(len(xyzs)):
            
            if i > j:
                
                j_coords = np.array(xyzs[j][1:]).astype(float)
                dist = np.linalg.norm(j_coords - i_coords)
                
                atom_i_label, atom_j_label = xyzs[i][0], xyzs[j][0]
                key1 = atom_i_label + atom_j_label
                key2 = atom_j_label + atom_i_label
                
                if key1 in avg_bond_lengths:
                    i_j_bond_length = avg_bond_lengths[key1]
                elif key2 in avg_bond_lengths:
                    i_j_bond_length = avg_bond_lengths[key2]
                else:
                    i_j_bond_length = 1.0  # Default bonded distance
                
                if dist < i_j_bond_length * (1.0 + tolerance):
                    if (key1=='CO'or key1=='OC'):
                        I1.append(i)
                        J1.append(j)
                    if (key1=='NH'or key1=='HN'):
                        I2.append(i)
                        J2.append(j)
                    if (key1=='NC'or key1=='CN') and (i not in I1 and j not in J1) and (i not in J1 and j not in I1) :#and (i in I2 and j in J2) and (i in J2 and j in I2):
                        print (i,j)
                        I.append(i)
                        J.append(j)
    print ("1",I2,J2)
    print (I,J)
    file = open("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/atoms/%s.txt" % numb, "w+")
    for k in range(len(I)):
        #        print(I[k])
        if ((I[k] not in I1) and (I[k] not in J1) and (J[k] not in I1) and (J[k] not in J1)):# and (I[k] in I2) and (I[k] in J2) and (J[k] in I2) and (J[k] in J2)):
            print('Atoms', I[k], '-', J[k])
            file.write("%i  %i\n" % (I[k],J[k]))
    #                return (I[k],J[k])
    for k in range(len(I2)):
        print('Atoms', I2[k], '-', J2[k])
        file.write("%i  %i\n" % (I2[k],J2[k]))
    
    del I[:]
    del J[:]
    del J1[:]
    del I1[:]
    del J2[:]
    del I2[:]

avg_bond_lengths = {
    'HH': 0.74,
    'CC': 1.54,
    'NN': 1.45,
    'OO': 1.48,
    'FF': 1.42,
    'ClCl': 1.99,
    'II': 2.67,
    'CN': 1.47,
    'CO': 1.43,
    'CS': 1.82,
    'CF': 1.35,
    'CCl': 1.77,
    'CBr': 1.94,
    'CI': 2.14,
    'HC': 1.09,
    'HN': 1.01,
    'HO': 0.96,
    'HBr': 1.41,
    'HCl': 1.27,
    'HI': 1.61
}
def xyzfile2xyzs(xyz_filename):
    
    xyzs = []
    i = 0
    
    for line in open(xyz_filename, 'r'):
        i += 1
        if len(line.split()) == 4 and i > 2:
            xyzs.append(line.split())

    return xyzs


def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", action='store', help='.inp file(s) sumbit to the queue', nargs='+')
    
    return parser.parse_args()


if __name__ == '__main__':
    
    #    args = get_args()
    #    for filename in args.filenames:
    #
    #        xyzs = xyzfile2xyzs(filename)
    #        xyz_bonds(xyzs)
    
    
    file_list = glob("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/solvent*.xyz")
    all_files = []
    for file in os.listdir("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/"):
        if file.endswith(".xyz"):
            all_files.append(os.path.join("/Users/matina/Desktop/Conf-Opt/1urea/LowestEnergy/xyz/", file))
    all_files.sort(key=natural_keys)


for k in range(len(all_files)):
    
    p=all_files[k].split('/')
    p=p[8].split('.')
    numb=p[0]
    print (p[0])
    xyzs = xyzfile2xyzs(all_files[k])
    xyz_bonds(xyzs,numb)
