#this is the main executable python script named checkPDB.py 

#!/usr/bin/env python 

import os  #this module check is the PDB file exists in the operation system using file path
import re  #module for regular expressions 
import requests 
import matplotlib.pyplot as plt 

#from package PDBTools import the module pdblib 
from PDBTools import pdblib 

#usr_prompts 
#while loop to continuously prompt for user input if the first is not good it keeps on continuing 
while True:
    #prompts for a user input 
    user_input = input("Welcome to PDBTools!\nEnter your query or press Enter to display the functionalities:")
    
#if no user input is given to the script, a helpful description of the tool's possibilities, it displays a menu of the program and to choose options  
    if not user_input:
        print("To start with, you will enter a PDB ID of your choice.")
        print("Then you choose any options by typing the number that corresponds to each data you want in the PDB file")
    
        #list each of the functionalities with a number to select that option 
        print("Press number 1 to get the HEADER.\nPress number 2 to get the TITLE.\nPress number 3 to get the SOURCE.")
        print("Press number 4 to get the KEYWORDS.\nPress number 5 to get the AUTHOR.\nPress number 6 to get the RESOLUTION.\nPress number 7 to get the JOURNAL TITLE\nPress number 8 to display the single-letter protein residues\nPress number 9 to write the sequence to a FASTA file\nPress number 10 to get lines starting with TAOM or HETATM, read or write the lines to a file\nPress number 11 to alter a chain ID from the PDB structure\nPress number 12 to find any non-standard protein residues\nPress number 13 to plot the temperature factor")
         
        #raise error if pdb id is not the correct type 
        while True:
            #first prompt for the PDB id
            pdb = input("Enter a PDB ID:")
            if len(pdb) != 4:
                print("Invalid PDB ID. Enter a 4-character long string e.g 1HIV")
            elif not pdb.isupper():
                print("Invalid PDB ID. The characters should be uppercase e.g. 1HIV.")
                #checks for at least one number and one letter in the PDB ID and then pass 
            elif not re.match("(?=.*[A-Z])(?=.*[0-9])[A-Z0-9]*$", pdb):
                print("Invalid PDB ID. The characters should be alphanumeric e.g. 1HIV")
            else:
                break 
                        
        #if the pdb file is present locally in the machine 
        # defining a function to check if the PDB file exists locally 
        def pdb_check(pdb):
            filename = f"{pdb.upper()}_project.pdb"
        #return the filename is it exists
            return os.path.exists(filename)
        
        #if the PDB file exists print a message to the user 
        if pdb_check(pdb):
            print("The PDB file is present locally.")

        #if the pdb is not found locally, call the function that downloads the PDB file from the module
        #call the function get_pdb 
        else:
            try:
                get_file = pdblib.get_pdb(pdb)
                print("PDB file is not present locally. Downloading the pdb file.....")
            # Download the PDB file by calling the get_pdb function from the module script using the module imported 
           
        #if PDB ID does not exists, use exception handling to avoid URL HTTPError      
            
            except requests.exceptions.HTTPError as er:
                if er.response.status_code == 404:
                        print("No such PDB ID exists in the RCSB database.\nEvery experimental structure in the PDB is assigned a 4-character alphanumeric identifier called the PDB identifier or PDB ID (e.g.2HBS).\nCheck for a valid PDB ID on the website")
                continue  
                 
        while True:
            #prompts for a selection based on the menu 
            usr_num = input("Enter a number to select the details or the task you want to perform on the PDB file:")
            if usr_num == '1':
            #print("Header:")
            #call the read_pdb function using the PDB ID as user input 
         
                details = pdblib.read_pdb(pdb)
        ##call the function get_header from the module that reads the file and get the HEADER value 

                header = pdblib.get_header(details)
            # Print the header value
                print("Header:", header)    
    
            elif usr_num == '2':
                details = pdblib.read_pdb(pdb)
                title = pdblib.get_title(details)
                if len(title) > 80:
                    new_tlt = ''
                    new_tlt += '\n'.join([title[i:i+80] for i in range (0, len(title), 80)])
                print("Title:",new_tlt)
            elif usr_num == '3':
                details = pdblib.read_pdb(pdb)
                source = pdblib.get_source(details)
                if len(source) > 80:
                    new_source = ''
                    new_source += '\n'.join([source[i:i+80] for i in range(0, len(source), 80)])
                    print("Source:", new_source)
            elif usr_num == '4':
                details = pdblib.read_pdb(pdb)
                keyword = pdblib.get_keyword(details)
                print("Keyword:", keyword)
            elif usr_num == '5':
                details = pdblib.read_pdb(pdb)
                author = pdblib.get_author(details)
                print("Author:",author)
            elif usr_num == '6':
                details = pdblib.read_pdb(pdb)
                res = pdblib.get_resolution(details)
                print("Resolution:",res)
            elif usr_num == '7':
                details = pdblib.read_pdb(pdb)
                journal = pdblib.get_journal(details)
                if len(journal) > 80:
                    new_journal = ''
                    new_journal += '\n'.join([journal[i:i+80] for i in range(0, len(journal), 80)])
                print("Journal title:", new_journal)
        
        
            elif usr_num == '8':
                
                protein_seq = pdblib.protein_residue(pdb)
                print("\n")
             
            elif usr_num == '9':
                print("If you don't know the chain ID, Press Enter. The chain IDs for the file will be displayed")
                fasta_file = pdblib.write_fasta(pdb)
                print("\nWriting the FASTA file.....")


            elif usr_num == '10':
                lines_atm_htm = pdblib.extract_lines(pdb)
                print("Writing lines to a file....")

            elif usr_num == '11':
                change_chainID = pdblib.alter_chainID(pdb)
                print("Changing the chain ID and saving to file....")

            elif usr_num == '12':
                print("Retrieving any non standard protein residue names...")
                non_standard_residues = pdblib.non_residues(pdb)
                
        
            elif usr_num == '13':
                print("Plotting the temperature factor....")
                plotting_temperature = pdblib.plot_temperature(pdb)
                
            elif usr_num > '13':
                print("Number given is beyond the options limit, enter a numerical value between 1-13")
                
            
            leave = input("Quit program[Yes/No]").capitalize()
            if leave == 'No':
                continue 
            elif leave == 'No':
                print("Exiting program....")
            break   
             
        else:
            print("Enter a numerical value")
    
    #Exiting the program only if the user inputs the word "quit", the letter "q" or the letter "Q". (1 mark)
    elif user_input == 'quit' or 'q' or 'Q':
        print("Exiting program.")
    break  # Exit the loop if user enters quit, q, or Q

else:
    print("You have a query")
    # if there is an input either PDB id or number 
    # Your code for handling the user's query goes here


