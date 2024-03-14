# PDBTools
This repository contains a package which contains a module which downloads, reads and query data from PDB files
Include a markdown file named "README.md" that: (1 mark)
  - explains what your software does, (1 mark)
  - shows how to create the conda environment (remember the "requests" module), and (1 mark)
  - how to retrieve it from GitHub (1 mark)
  - how to run your script. (1 mark)
  - Use markdown syntax (1 mark)



'''The following commands (mkdir, conda create, conda env list, conda activate ... were run in the terminal) 

'''

#creating a 'miniproject' directory for the packages and modules of the project 
mkdir miniproject  

#creating a conda env named py311 
conda create -n py311 conda-forge::jupyterlab python=3.11

#listing the availble environments 
conda env list
#output for the conda environments:                                                                                                                                                                                                                                        
#py311                    /home/ubuntu/.conda/envs/py311                                                                            
#base                     /home/ubuntu/bin/miniconda  

#activating the py311 env 
conda activate py311

#ubuntu@ubuntu-Precision-3570:~/Python_exercises$ conda activate py311
#(py311) ubuntu@ubuntu-Precision-3570:~/miniproject$   

