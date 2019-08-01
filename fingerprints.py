from __future__ import print_function
import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Torsions
from rdkit.Chem.Pharm2D import Gobbi_Pharm2D,Generate
import numpy
import pandas as pd
bi1={}
bi2={}

suppl = Chem.SmilesMolSupplier('Desktop/cat.smi')
mols = [x for x in suppl]
len(mols)
a=mols[1]
print(Chem.MolToSmiles(a))

suppl1 = Chem.SmilesMolSupplier('Desktop/sub.smi')
mols1 = [x for x in suppl1]
len(mols1)

bi1=[]
fps1=[]
for x in mols:
    bi={}
    fps=AllChem.GetMorganFingerprintAsBitVect(x, radius=2, bitInfo=bi)
    bi1.append(bi)
    fps1.append(fps)

bi2 = []
fps2 = []
for x in mols1:
    bi = {}
    fps = AllChem.GetMorganFingerprintAsBitVect(x, radius=2, bitInfo=bi)
    print(fps)
    bi2.append(bi)
    fps2.append(fps)
A=[]
B=[]
A= numpy.mat(fps1)
B=numpy.mat(fps2)


df=pd.read_csv('Documents\list.csv', sep=',',header=None)
df.columns=['Substrate','Catalyst', 'Solvent','Temp']

cat=pd.read_csv('ORCA-cat.csv', sep=',',header=None)

a1=[]
b1=[]

cat=cat.as_matrix(columns=None)

d=numpy.empty([257,4159])
for index, row in df.iterrows():
    a=row['Substrate']
    b=row['Catalyst']
    f=row['Solvent']
    g=row['Temp']
    a1=numpy.array(B[a])
    print(a1)
    b1=numpy.array(A[b])
    print(b1)
    b2=numpy.array(cat[b])
    c=numpy.concatenate((a1, b1,b2,f,g), axis=None)
    print(c)
    d[index]=c

numpy.savetxt("FullDataFingerprintsorca.csv", d, delimiter=",")