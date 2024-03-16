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
 ''' this function reads the PDB file given a PDB ID and returns each line as a list of strings which is then parsed''' 
    with open(f'{PDBid}_project.pdb', 'r') as file:
        PDB_file = file.readlines()  #reads the whole file as a list of strings   
        
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


#defining a function to get the single letter protein residue 
def protein_residue(PDBid):
    def read_pdb(PDBid):
        with open(f'{PDBid}_project.pdb', 'r') as file:
            return file.readlines()  # Read the file line by line and returns each line as a list of strings
    #user input for  a chain ID
    chain_ID = input("Enter a chain ID:")
    print("Retrieving single letter residues.....")
    #statement to check the chain ID
    if chain_ID in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        #get the lines starting with ATOM
        #call the read_pdb function 
        lines = read_pdb(PDBid)
        for line in lines:
            if line[:4] == 'ATOM' and 'CA' in line and line[21] == chain_ID:
                #get the lines with the chain 
                #get the residues 
                residue = line[17:20] 
                #Use a dictionary of the standard single residue code for each amino acid 
                res_code = {
                    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                    'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                    'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                    'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'
                }
                
                print(res_code.get(residue, 0), end ='')
    else:
        print("ENter a valid chain ID")



#defining a function to write a FASTA formatted file and get the single letter protein residue 
def write_fasta(PDBid,chain_ID):
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
        
    #call the read_pdb function to get the sequences for the chain ID requested 
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
    #print message invalid chain ID or chain ID does not exist in the file
            print(f"Chain {chain_ID} does not exist in the file")

#defining a function extract_lines to extract lines with ATOM or HETATM
def extract_lines(PDBid,chain_ID):
    def read_pdb(PDBid):
        with open(f'{PDBid}_project.pdb', 'r') as file:
            return file.readlines()
    
     # Read the file line by line and returns each line as a list of strings
     #parse the PDB file and get all lines starting with ATOM or HETATM record type

    lines = read_pdb(PDBid) 
    lines_atm = []
    lines_htm = []
    for line in lines:
        if line[:4] == 'ATOM' and line[21] == chain_ID:
            lines_atm.append(line.strip())
        elif line[:6] =='HETATM' and line[21] == chain_ID:
            lines_htm.append(line.strip())
        #return lines_atm, lines_htm


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
#find the index of chain ID based on the user input, change all instances of that chain ID using .replace method

def alter_chainID(PDBid):
    ''' this function will find the index of chain ID based on the user input, change all instances of that chain ID using indexing'''
    new_chainIDS = []
    with open(f'{PDBid}_project.pdb', 'r') as file:

        lines = file.readlines()  # Read the file line by line and returns each line as a list of strings
        #parse the PDB file and get all lines starting with ATOM or HETATM record type

        chain_ID = input("Enter a chain ID you want to change:")
        #statement to check the chain ID
        if chain_ID in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            new_ID = input("Enter the change you want to make e.g A to M:").upper()
        else:
            print("Invalid chain ID or chain does not exists")
        #creating an empty list to store the modified lines with the new IDs
        mod_lines = []
        for line in lines:
            #get all the chain IDs for the PDB file
            if line[:4] == 'ATOM' or line[:6] == 'HETATM':
                #extracting all the chain IDS from each line
                chainID = line[21]
                #statement to check the chain ID
                if chainID == chain_ID:

                #replace all instances of line[21] with a random letter
                    new_IDs = new_ID
                    line = line[:21] + new_IDs + line[22:]
                    new_chainIDS.append(new_IDs)
            #appending lines to a new modidied file
            mod_lines.append(line)
    # Write modified lines to a new file
    with open(f'{PDBid}_modified.pdb', 'w') as modified_file:
        modified_file.writelines(mod_lines)

    return new_chainIDS

#non standard protein residues are HOH, inhibitors or cofactors which are in record type HETATM

def non_residues(PDBid):
    '''this function retrieves any non standard protein residue names from the PDB file '''
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
                    non_std_res.add(residue)
    if non_std_res:
        print("Non standard protein residue names are:\n")
        print('  '.join(non_std_res))

    else:
        print("No non-standard residues found.")

import matplotlib.pyplot as plt 

def plot_temperature(PDBid):
    #to get one entry per residue use set to get only unique non std residues
    with open(f'{PDBid}_project.pdb', 'r') as file:
        lines = file.readlines()  # Read the file line by line and returns each line as a list of strings

#look for index temperature for each line starting with ATOM
        chain_id = input("ENter a chain ID:")
        #plot_dim = input("Enter the plot dimensions e.g tuple (10,4):")
        atoms = []
        temperatures = []
        for line in lines:
            if line[:4] == 'ATOM' and line[21] == chain_id:
                temp = float(line[60:66].strip())
                #get only the backbone atoms of the protein
                atom = line[5:11].strip()
                atoms.append(atom)
                temperatures.append(temp)

                #print(residues, temp)
        plot_dim = input("Enter the plot dimension e.g tuple 10,4:")
        #plot the line graph of residues against temperature factor
        fig, ax = plt.subplots(figsize=eval(plot_dim))
        ax.plot(atoms,temperatures, 'red')
        ax.set_ylabel("Temperature factor")
        ax.set_xlabel("atoms")
        ax.set_xticks(atoms[::11])
        ax.set_xticklabels(atoms[::11], rotation='vertical')
        ax.set_title("Temperature factors of the chain" + ' ' + chain_id)

        # Save the plot to a file
        plt.tight_layout()
        plt.show
        fig.savefig(f"{PDBid}_temp_factor_plot.png", dpi=300)
        #saving the figure to an output file
        
