#This is a Python script named pdblib.py which contains all the functions to read, parse and extract data from the PDB file  
#!/usr/bin/env python


#the pdblib.py module which contains 3 main functions that downloads, parse and get the query 

import requests
 
# if pdb file is not present  locally
#calling the function get_pdb 

#defining a function named get_pdb 
def get_pdb(PDBid):
    ''' this function downloads a pdb ID from the RCSB site which takes as positional argument a PDB ID'''
    #using the requests module constructing the URL to retrieve any PDB structure file from user input 
    file = requests.get("https://files.rcsb.org/download/"+ PDBid +".pdb")
    #get the status of the file 
    file.raise_for_status()
    #get the PDB file downloaded in the local machine 
    pdb_file = file.content 
    
    #get the PDB file saved to local disk with option write and modify 
    with open(f'{PDBid}_project.pdb','wb') as dfile:  
     #_project given to saved files not to overwrite existing PDB files
        dfile.write(pdb_file)
     #display a message to the user 
        print("PDB file downloaded successfully and saved to local disk")
        
#defining a function that reads and parse the PDB file requested 

def read_pdb(PDBid):
    ''' is function reads the PDB file given a PDB ID and returns each line as a list of strings which is then parsed'''
    with open(f'{PDBid}_project.pdb', 'r') as file:
        PDB_file = file.readlines()  #gets the whole file as a list of strings   
        
    #creating an empty dictionary named details to store key:value pairs of details from the PDB file 
    details = {"Header": "", "Title": "","Source": "", "Keywords": "","Author": "", "Resolution": "","Journal": ""}

    #for loop to iterate over each line in the PDB file 
    for line in PDB_file:
     
     #use slice indexing to check if the first 6 characters is equal to "HEADER"
        if line[:6] == "HEADER":
         #add the header as key and the header details removing any whitespaces
         #and add header details as value to the dictionary
            details["Header"] += line[10:].strip()
        
        #if the first 5 chars equal to "TITLE"
        elif line[:5] == "TITLE":
         #add the title as key and title details as value to the dictionary 
            details["Title"] += line[10:].strip() + ' '
         
        elif line[:6] == "SOURCE": 
            details["Source"] += line[10:].strip()
                
        elif line[:6] == "KEYWDS":
            details["Keywords"] += line[10:].strip()
         
        elif line[:6] == "AUTHOR":
            details["Author"] += line[10:].strip()
        
       #if the first 6 chars equal to "REMARK" and the string '2 RESOLUTION' is in the line
        elif line[:6] == "REMARK" and '2 RESOLUTION' in line:
         #add the key Resolution and the details as from char index 22 as values to the dictionary 
            details["Resolution"] += line[22:].strip()
         
        elif line[:4] == "JRNL" and 'TITL' in line:
            details["Journal"] += line[18:].strip() + ' '
    #return the dictionary    
    return details  

#creating a function for each detail using the dictionary to access the key and values
def get_header(details):
    ''' get_header function, when called, will extract and return the values for key named Header'''
    #return the values for Header 
    return details["Header"]

def get_title(details):
    ''' get_title function, when called, will return the values for key named Title'''
    return details["Title"]

def get_source(details):
    ''' get_source function, when called, will return the values for key named Source'''
    return details["Source"]

def get_keyword(details):
    ''' get_keyword function, when called, will return the values for key named Keyword'''
    return details["Keywords"]
 
def get_author(details):
    ''' get_author function, when called, will return the values for key named Author'''
    return details["Author"]

def get_resolution(details):
    ''' get_resolution function, when called, will return the values for key named Resolution'''
    return details["Resolution"]
 
def get_journal(details):
    ''' get_journal function, when called, will return the values for key named Journal'''
    return details["Journal"]


#defining a function to get the single letter protein residues 
def protein_residue(PDBid,chain_ID): 
    ''' this function opens, reads the PDB file given a PDB id and chain_ID as input'''
    def read_pdb(PDBid):
        with open(f'{PDBid}_project.pdb', 'r') as file:
            return file.readlines()  # Read the file line by line and returns each line as a list of strings
    
    #statement to check if the chain ID exists or not setting flag to False before reading the lines  
    chain_found = False 
    #storing each line in variable lines used for parsing 
    lines = read_pdb(PDBid)
    #loop that iterates over each line 
    for line in lines:
        #if each line has string 'ATOM' as first four characters and string 'CA' is in the same line
        if line[:4] == 'ATOM' and 'CA' in line:
         #index slicing the chain IDs from each line with ATOM and CA and storing in variable chain_ind 
            chain_ind = line[21]
         
                #get the 3-letter residues using slice indexing  
            residue = line[17:20]
                #Use a dictionary of the standard single residue code for each amino acid 
            res_code = {
                    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                    'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                    'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                    'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'
                }
            #check if the chain ID given by user is equal to the chain_ind in the file 
            if chain_ind == chain_ID:
             #raise flag to True if found 
                chain_found = True
             #get the single letter code (values) for each residue storing them in sequence 
                sequence = res_code.get(residue, 0)
                print(sequence, end ='')
    #if the chain ID is not found 
    if not chain_found:
        #print a message to user 
        print(f"Chain {chain_ID} does not exist in the file")


#defining a function named write_fasta 
def write_fasta(PDBid,chain_ID):
    ''' this function parse PDB file and write a FASTA formatted file with the single letter protein residues given a PDBid and chain ID as input ''' 
    def read_pdb(PDBid):
        with open(f'{PDBid}_project.pdb', 'r') as file:
            return file.readlines()  # Read the file line by line and returns each line as a list of strings
  
    #if no chain is given e.g user input has no arguments 
    if chain_ID == "": 
        print("No chain ID is provided, the existing chains will be retrieved")
        #save each chain as an entry in a single fasta file
        #extract all the chain IDs from the PDB file 
        lines = read_pdb(PDBid)
        #creating an empty dictionary to store all the chain IDs present and their sequences extracted from the PDB file 
        chain_sequences = {}
        for line in lines:
            #get all the chain IDs for the PDB file 
            if line[:4] == 'ATOM' and 'CA' in line:
                #extracting all the chain IDS from each line 
                chain_ID = line[21]
                if chain_ID not in chain_sequences:
                    chain_sequences[chain_ID] = '' #creating keys 
                #get the residues 
                residue = line[17:20]
                res_code = {
                            'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                            'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                            'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                            'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'}
            
                chain_sequences[chain_ID] += res_code.get(residue, 0)  #adding the the values to each chain ID
            elif line.startswith("HEADER"):
                header = line[10:].strip()

                #write to output file each chain as an entry
        with open(f'{PDBid}chainID.fasta', 'w') as cfile:
            cfile.write(f'>{header}\n')
        #loop through the created dictionary and get the sequence(value) for each chain(key)
            for chain_ID, sequence in chain_sequences.items():
            #write to output file each chain as an entry
                with open(f'{PDBid}chainID.fasta', 'a') as cfile:
                    cfile.write(f'Chain{chain_ID}:{sequence}\n')
                    print(f"Chain {chain_ID}: {sequence}")
        
    #otherwise, if user gives an input, call the read_pdb function to read the PDB file and get the sequences for the chain ID requested 
    else:
            
        lines = read_pdb(PDBid)
        sequence = ''
        chain_found = False 
        for line in lines:
        
        #get the lines starting with ATOM and only CA atoms with corresponds to the chain ID 
        #get the lines for that chain 
                 
            if line[:4] == 'ATOM' and 'CA' in line:
                #get the residues 
                residue = line[17:20] 
                chain = line[21] 
                #Use a dictionary of the standard single residue code for each amino acid 
                res_code = {
                        'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                        'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                        'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                        'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V' }
                if chain == chain_ID:
                    chain_found = True 
                #for each residue get their corresponding single letter protein letter
                    print(res_code.get(residue, 0), end="")
            #store the letters in sequence (empty string)
                    sequence += res_code.get(residue, 0)
                
            elif line.startswith("HEADER"):
                header = line[10:].strip()
                output_filename = input("Enter the output filename for that chain e.g 1HIV_sequence:")
                print(f"Retrieving the sequence for chain ID...:{chain_ID}")
                
            # saving the sequence retrieved for that chain in a fasta formatted file, given a chain ID and output filename 
            #write a fasta file using the PDB header, and chain IDs as definition line 
            with open(f'{output_filename}.fasta', 'w') as f_file:
                f_file.write(f'>{header}   chain_ID:{chain_ID}\n{sequence}')
        #if parsing all lines in the files and does not find the chain ID
        if not chain_found:
            print(f"Chain {chain_ID} does not exist in the file")

#defining a function named extract_lines to extract lines with ATOM or HETATM
def extract_lines(PDBid,chain_ID):
    ''' this function will extract lines with ATOM or HETATM and either write or read the relevant lines to an output file based on user input '''
    def read_pdb(PDBid):
        with open(f'{PDBid}_project.pdb', 'r') as file:
            return file.readlines()
    
     # Read the file line by line and returns each line as a list of strings
     #parse the PDB file and get all lines starting with ATOM or HETATM record type
    chain_found = False 
    lines = read_pdb(PDBid) 
   #creating empty lists to store the lines with ATOM and HETATM
    lines_atm = []
    lines_htm = []
   #for loop iterates through each line and get lines with ATOM and finds the chain_IDs 
    for line in lines:
        if line[:4] == 'ATOM' and line[21] == chain_ID:
         #if the chain ID given by user is found add the lines with ATOM to the empty list removing spaces
            chain_found = True 
            lines_atm.append(line.strip())
         #if the chain ID is found add lines with HETATM to the empty list 
        elif line[:6] =='HETATM' and line[21] == chain_ID:
            chain_found = True 
            lines_htm.append(line.strip())
   #if parsing all lines in the files and does not find the chain ID
     if not chain_found:
            print(f"Chain {chain_ID} does not exist in the file")
         
    #check each user input and read or write the lines to the file
    #give the user the choice between writing and reading to a file

    usr_inp = input("Press letter 'R' to read the file, or letter 'W' to write to file: ").upper()
    usr_choice = input("Enter the record type (ATOM or HETATM): ").upper()
    if usr_inp == 'R':
        #ask for ATOM or HETAM, print the relevant lines
        if usr_choice == 'ATOM':
            print(str(lines_atm))
        elif usr_choice == 'HETATM':
            print(str(lines_htm))


    elif usr_inp == 'W':
        #write the lines to the file
        with open(f'{PDBid}.txt', 'w') as outfile:
            if usr_choice == 'ATOM':
                for line in lines_atm:
                    #writing ATOM lines
                    outfile.write(line + '\n')
            elif usr_choice == 'HETATM':
                # Write HETATM lines
                for line in lines_htm:
                    outfile.write(line + '\n')

#defining a function to alter a chain ID
def alter_chainID(PDBid,chain_ID):
    ''' this function will find the index of chain ID based on the user input, change all instances of that chain ID using indexing'''
    new_chainIDS = []
    with open(f'{PDBid}_project.pdb', 'r') as file:
        chain_found = False
        lines = file.readlines()  # Read the file line by line and returns each line as a list of strings
        #parse the PDB file and get all lines starting with ATOM or HETATM record type
        #prompts user for a new chain ID 
        new_ID = input("Enter the new chain ID:").upper()

        #creating an empty list to store the modified lines with the new IDs
        mod_lines = []
        for line in lines:
            #get all the chain IDs for the PDB file
            if line[:4] == 'ATOM' or line[:6] == 'HETATM':
                #extracting all the chain IDS from each line
                chainID = line[21]
                #statement to check the chain ID
                if chainID == chain_ID:
                    chain_found = True
                 #replace all instances of line[21] with a random letter
                    new_IDs = new_ID
                    line = line[:21] + new_IDs + line[22:]
                    new_chainIDS.append(new_IDs)
            #appending lines to a new modidied file
            mod_lines.append(line)
        print(f"Changing chain id from {chain_ID} to {new_ID} ")
        print(f"Writing to output file.....")

        if not chain_found:
            print(f"Chain {chain_ID} does not exist in the file")
# Write modified lines to a new file
    with open(f'{PDBid}_modified.pdb', 'w') as modified_file:
        modified_file.writelines(mod_lines)

    return new_chainIDS


#defining a function named non_residues 
def non_residues(PDBid):
    '''this function retrieves any non standard protein residue names from the PDB file '''
    #non standard protein residues are HOH, inhibitors or cofactors which are in record type HETATM
    #to get one entry per residue use set to get only unique non std residues 
    non_std_res = set()
    with open(f'{PDBid}_project.pdb', 'r') as file:

        lines = file.readlines()  # Read the file line by line and returns each line as a list of strings
        
     #look for index residue [17:20] in each line and get those which are not in the list of standard residues 
        for line in lines:
            if (line[:4] == 'ATOM' or line[:6] == 'HETATM'):
                residue = line[17:20].strip()
            #create a list of standard amino acids 
                std_res = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
                if residue not in std_res:
                 #get those which are not in the list of standard residues 
                    non_std_res.add(residue)
    if non_std_res:
        print("Non standard protein residue names are:\n")
        print('  '.join(non_std_res))

    else:
        print("No non-standard residues found.")

import matplotlib.pyplot as plt 
#defining a function named plot_temperature 
def plot_temperature(PDBid,chain_ID,plot_dim):
    ''' this function will plot the temperature factor of atoms given a PDB ID, chain ID and plot dimensions as input ''' 
    with open(f'{PDBid}_project.pdb', 'r') as file:
        lines = file.readlines()  # Read the file line by line and returns each line as a list of strings

        #creating empty lists to contain the atoms and temperature values 
        atoms = []
        temperatures = []
        #set the chain_found to False before iterating through the lines 
        chain_found = False
        for line in lines:
            if line[:4] == 'ATOM' and line[21] == chain_ID:
                chain_found = True
             #get the index of temperature values in the file 
                temp = float(line[60:66].strip())
                #get only the backbone atoms of the protein
                atom = line[5:11].strip()
                atoms.append(atom)
                temperatures.append(temp)

                #print(residues, temp)
        if not chain_found:
            print(f"Chain {chain_ID} does not exist in the file")

        #plot the line graph of residues against temperature factor
        fig, ax = plt.subplots(figsize=(plot_dim))
        #setting the plot x and y-axes labels 
        ax.plot(atoms,temperatures, 'red')
        ax.set_ylabel("Temperature factor")
        ax.set_xlabel("atoms")
        #setting the scale with a step value of 100 atoms 
        ax.set_xticks(atoms[::100])
        ax.set_xticklabels(atoms[::100], rotation='vertical')
        ax.set_title("Temperature factors of the chain" + ' ' + chain_ID)
        # Save the plot to a file
        plt.tight_layout()
        plt.show
        fig.savefig(f"{PDBid}_temp_factor_plot.png", dpi=300) #saving the figure to an output file

        
