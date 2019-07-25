# CatalystDesign
A computer aided workflow for catalyst design.
This workflow is designed to computationally calculate properties for hydrogen-bonding catalysts. For each catalyst physical, chemical and structural descriptors are calculated and then given as an input to a machine learning (ML) model. The aim is to use the knowledge gained from previous analysis to predict the reactivity of new catalysts. The code is written in Python 3. MatLab is used for the ML analysis.

Dependencies:

• rdkit • numpy • ORCA v. 4.1 • XTB v. 6.1 • OpenBabel • MatLab

The scripts are used as follows:

For the physical and chemical descriptors

a) The SMILES strings of the catalysts are used as an input for "smileTopdb.py". The user has to give a .txt file with SMILE strings of interest and the pdb files will be created.

b) The catalysts are fitted to the core with "FitWithRDKIT.py". The user gives as an input the pdb files and a core.sdf. New pdb files will be created.

c)The fluoride ion is added to the pdb files with "add_F.py". It will always be placed at the end of the file. The pdb files of the catalysts and the coordinates of the fluoride ion are needed as an input.

d)To generate conformers XTB v. 6.1 is used. The pdb files of the catalyst-fluoride complex, are converted to xyz files with OpenBabel ("obabel filename.pdb -O filename.xyz") and given to XTB.

e) A series of .scoord files will be created. "coord2xyz.py" is used to convert them to xyz files.

f) Some of the conformations will be irrelevant, "accessible_F.py" excludes these conformations. The xyz files are needed as inputs.

g) Some of the remaining conformations will be very similar to each other, "rmsdexclude.py" will exclude conformations that differ for less than 1Å. The script reads pdb files so OpenBabel is used again ("obabel filename.xyz -O filename.pdb").

h) Single point energies at the PBE-D3BJ/def2-SVP level of theory are calculated with ORCA. "ORCAmin.py" generates the input files. As an input the xyz files of the conformations of interest are needed.

i) The conformations are weighted according to Boltzmann's distribution. "Boltzmann.py" takes as an input the output files from ORCA and returns as an output a csv file, with the conformations that contribute up to 90%.

j) Optimizations at the same level of theory are performed, for the conformers that contribute up to 90% of the population. “ORCA_input1.py” generates the input files. As an input the xyz files of the conformations of interest are needed.

k) The final single point energies are sorted with “Energy_sort.py” which uses as an input the output files of the ORCA calculations and returns a csv file with the lowest energy conformer.

l) Single point energy corrections at the PBE-DEBJ/def-TZVP level of theory are calculated only for the lowest energy conformations. “ORCA_input2.py” generates the input files. As an input the xyz files of the conformation of interest are needed.

m) From the output files, electronic descriptors are extracted with “descriptors.py”.

For the structural descriptors

To calculate Steric parameters we slightly altered the Paton and co-workers code [1].

n) To identify the atoms for which we wish to calculate Steric parameters upon, “connectxyz.py”, uses as an input the xyz files of the optimized complexes. The script automatically identifies the carbon and hydrogen atoms that are connected to the nitrogen atoms of the ureas, returning a list of atom ids for each catalyst.

o) L, B1 and B5 values are calculated with “sterimol.py” (it automatically calls “sterimoltools.py”). The script takes as an input the pdb files of the optimized catalysts.


[1]	A. V. Brethomé, S. P. Fletcher, and R. S. Paton, "Conformational Effects on Physical-Organic Descriptors–the Case of Sterimol Steric Parameters," ACS Catalysis, 2019.

For the ML model

The above descriptors are given to MatLab
