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
- Open your bash temrinal and run the following commands to create a new conda environment named "py311" with Python 3.11

*mkdir* , *conda create*, *conda env list*, *conda activate* are to be used in the terminal

Note: Ensure that Conda is installed and the Conda command is available in the terminal 

- creating a 'miniproject' directory for the packages and modules of the project 
*mkdir* miniproject  

- creating a conda env named py311 
  conda create* -n py311 python=3.11

-listing the availble environments 
*conda env list*

- activating the py311 env 
*conda activate* py311
 
- Install the "requests" module using sudo apt-install
*sudo apt-install* requests

- Install Matplotlib to plot graphs
*sudo apt-install python3-matplotlib*

### How to retrieve the repository from GitHub
go to your working directory e.g miniproject and run the git clone command followed by the URL

*git clone* https://github.com/username/PDBTools.git 
you will now see a PDBTools repository and a PDBTools package as subdirectories to miniproject 

### How to run the executable script named 'checkPDB.py'
#go to your directory where the script is found and run the following commands:
*chmod* +x checkPDB.py 
*python* checkPDB.py 
