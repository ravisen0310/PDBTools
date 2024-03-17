# PDBTools

Include a markdown file named "README.md" that: (1 mark)
  - explains what your software does, (1 mark)
  - shows how to create the conda environment (remember the "requests" module), and (1 mark)
  - how to retrieve it from GitHub (1 mark)
  - how to run your script. (1 mark)
  - Use markdown syntax (1 mark)

### What the software does 
This repository named PDBTools contains a package named PDBTools which contains a module named pdblib.py which downloads, reads and query data from PDB files



### How to create a conda environment 
The following commands:
*mkdir* , *conda create*, *conda env list*, *conda activate* were run in the terminal


#creating a 'miniproject' directory for the packages and modules of the project 
mkdir miniproject  

#creating a conda env named py311 
conda create -n py311 python=3.11

#listing the availble environments 
conda env list

#output for the conda environments: 
Should be (py311)  

#activating the py311 env 
conda activate py311

