from __future__ import print_function

import numpy
import pandas as pd

#Open Reaction Matrix List

df=pd.read_csv('/mnt/d/Sterimol/CatDesign/List.csv', sep=',',header=None)
df.columns=['Substrate','Catalyst', 'Solvent','Temp']

#Import catalyst and substrate descriptors
cat=pd.read_csv('/mnt/d/Sterimol/Examples/Model5/Orcacats.csv', sep=',',header=None)
sub=pd.read_csv('/mnt/d/Sterimol/Examples/sub_lowest_xyz/SUBSTRATES_Matrix.csv', sep=',',header=None)

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
numpy.savetxt("/mnt/d/Sterimol/Model5Toms.csv", d, delimiter=",")





