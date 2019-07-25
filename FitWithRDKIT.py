import os
import re
from rdkit import Chem
from rdkit.Chem import AllChem

all_files = []
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
for file in os.listdir("/Users/matina/Desktop/catalysts_80_pdb/"):
     if file.endswith(".pdb"):
         print(os.path.join("/Users/matina/Desktop/catalysts_80_pdb/", file))
         all_files.append(os.path.join("/Users/matina/Desktop/catalysts_80_pdb/", file))
all_files.sort(key=natural_keys)
print (all_files)

for k in range(len(all_files)):
     with open(all_files[k]) as infile2:
        mol1 = Chem.MolFromPDBFile(infile2.name,removeHs=False)
        print(infile2.name)
        suppl = Chem.SDMolSupplier('/Users/matina/Desktop/core5.sdf')
        len(suppl)
        mol2 = suppl[0]
        if mol1.HasSubstructMatch(mol2):
            if AllChem.ConstrainedEmbed(mol1, mol2):
             print("ok")
             Chem.MolToPDBFile(mol1,'/Users/matina/Desktop/newc2/newc_%i.pdb' % k)
            else:
                continue
        else:
            continue

