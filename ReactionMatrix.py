from __future__ import print_function
import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

import numpy
import pandas as pd

#Open Reaction Matrix List

df=pd.read_csv('/Users/matina/Desktop/descriptors/List.csv', sep=',',header=None)
df.columns=['Substrate','Catalyst', 'Solvent','Temp']

#Import catalyst and substrate descriptors
cat=pd.read_csv('/Users/matina/Desktop/descriptors/CATALYSTS.csv', sep=',',header=None)
sub=pd.read_csv('/Users/matina/Desktop/descriptors/SUBSTRATES.csv', sep=',',header=None)

a=df.shape[0]
b=cat.shape[1]+sub.shape[1]+2
a1=[]
b1=[]

cat=cat.values
sub=sub.values

#Generate Reaction Matrix
d=numpy.empty([a,b])
for index, row in df.iterrows():
    a=row['Substrate']
    b=row['Catalyst']
    f=row['Solvent']
    g=row['Temp']
    a1=numpy.array(sub[a])
    print(a1)
    b1=numpy.array(cat[b])
    print(b1)
    c=numpy.concatenate((a1, b1,f,g), axis=None)
    print(c)
    d[index]=(c)


#save matrix
numpy.savetxt("/Users/matina/Desktop/descriptors/ORCA_All_Lowest.csv", d, delimiter=",")





