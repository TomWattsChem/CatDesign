from rdkit.Chem import AllChem
from rdkit import Chem
import os
import shutil

os.makedirs("/Users/matina/Desktop/tetraXTB/lessthan4/rmsd",exist_ok=True)
pdb_filenames = []
folder = '/Users/matina/Desktop/tetraXTB/lessthan4'
for filename in os.listdir(folder):
    if filename.endswith(".pdb") and not filename.startswith('.'):
        pdb_filenames.append(filename)

rmslist = []
count=0
mol_list = []
for pdb_filename in sorted(pdb_filenames):
    mol = Chem.MolFromPDBFile(os.path.join(folder, pdb_filename))
    mol_list.append(mol)

for mol in mol_list:
    rmslist.append(AllChem.AlignMol(mol_list[0], mol))

[print(filename) for filename in sorted(pdb_filenames)]
print(len(pdb_filenames))
print(len(rmslist))
print(rmslist)
for (j,k) in zip(rmslist,sorted(pdb_filenames)):
    if j>1.5:
        count=count+1
        print(j)
        print(k)
        shutil.move("%s/%s" %(folder,k), "/Users/matina/Desktop/tetraXTB/lessthan4/rmsd")
shutil.move("%s/%s" % (folder, (sorted(pdb_filenames))[0]), "/Users/matina/Desktop/tetraXTB/lessthan4/rmsd")
print (count)


exit()


