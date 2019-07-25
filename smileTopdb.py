from rdkit import Chem
from rdkit.Chem import AllChem

mol1 = Chem.MolFromSmiles('O=C(NC1=CC(C(F)(F)F)=CC(C(F)(F)F)=C1)N(C)C(C=C2)=[C@]([C@]3=C(C=CC=C4)C4=CC=C3NC(NC5=CC(C(F)(F)F)=CC(C(F)(F)F)=C5)=O)C6=C2C=CC=C6')
m1 = Chem.AddHs(mol1)
AllChem.EmbedMolecule(m1,useRandomCoords=True,enforceChirality=True)
Chem.rdmolfiles.MolToPDBFile(m1, "/Users/matina/Desktop/template_noF.pdb")

