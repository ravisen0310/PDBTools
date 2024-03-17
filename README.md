# PDBTools

Include a markdown file named "README.md" that: (1 mark)
  - explains what your software does, (1 mark)
  - shows how to create the conda environment (remember the "requests" module), and (1 mark)
  - how to retrieve it from GitHub (1 mark)
  - how to run your script. (1 mark)
  - Use markdown syntax (1 mark)

### What the software does 
This repository named PDBTools contains a package named PDBTools which contains a module named pdblib.py which downloads, reads and query data from PDB files
This software is search engine-based which prompts for a PDB ID, chain ID to retrieve protein-related data (e.g sequence, PDB file details such as journal title, keywords, authors....) 

- Once the script is executed, a welcome page will be displayed "Welcome to PDB Tools".
- The software first prompts the user to press Enter key to display the functionalities of PDBTools
- After pressing Enter, the user is prompted to input a PDB ID.
- Once a valid PDB ID is entered, the corresponding PDB file gets downloaded from RCSB if not present locally with suffix {PDB ID}_project.pdb
- After the download, the software reads the file and parse it to extract data selected by the user
- 13 numbered selections are provided to the user, where each number gives a functionality of the Tool by extracting data from the PDB file
- for e.g if the user press number 8, the single letter protein sequence will be retrieved and displayed given the user gives a chain ID as input
- the software reads the PDB file and extracting sequence: If the chain ID is valid, it extracts the sequence of amino acids for the specified chain.
- It uses the ATOM records to identify amino acids.
- User is prompted to input an output filename where sequences are written to a file
- the user can press q or Q or quit when prompted to enter a selection such that pressed once will exit the current prompt and goes back to the Welcome page and user and input a new PDB ID for a new query
- if pressed twice it will completely exit the software 


### How to create a conda environment 
- Open your bash temrinal and run the following commands to create a new conda environment named "py311" with Python 3.11

*mkdir* , *conda create*, *conda env list*, *conda activate* are to be used in the terminal

Note: Ensure that Conda is installed and the Conda command is available in the terminal 

- creating a 'miniproject' directory for the packages and modules of the project 

*mkdir* miniproject  

- creating a conda env named py311
  
*conda create* -n py311 python=3.11

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
