#this is the main executable python script named checkPDB.py 

#!/usr/bin/env python 

import os                        #module to check if the PDB file exists in the operation system using file path
import re                        #module to check for regular expressions 
import requests                  #module to retrieve URL 
import matplotlib.pyplot as plt  #module to plot graphs/figures 

from PDBTools import pdblib      #importing the module pdbib (containing all functions to read, parse and extract data) from the package PDBTools

#while loop to continuously prompt for user input if the previous statements return False  
while True:
    #prompts for a user input 
    user_input = input("Welcome to PDBTools!\nPress Enter to display the Tool's functionalities:")
    
#if no user input is given to the script, a helpful description of the tool's possibilities, it displays a menu of the software and allow the user to select options  
    if not user_input:
        #display messages to guide the user 
        print("To start with, you will enter a PDB ID of your choice.")
        print("Then you choose any options by typing the number that corresponds to each data you want in the PDB file")
       
        #list each of the Tool's functionalities with a number to select that option 
        print("Press number 1 to get the HEADER.\nPress number 2 to get the TITLE.\nPress number 3 to get the SOURCE.")
        print("Press number 4 to get the KEYWORDS.\nPress number 5 to get the AUTHOR.\nPress number 6 to get the RESOLUTION.")
        print("Press number 7 to get the JOURNAL TITLE\nPress number 8 to display the single-letter protein residues\nPress number 9 to write the sequence to a FASTA file.")
        print("Press number 10 to get lines starting with ATOM or HETATM, read or write the lines to a file\nPress number 11 to alter a chain ID from the PDB structure.")
        print("Press number 12 to find any non-standard protein residues\nPress number 13 to plot the temperature factor.")

    
        #display a message to document the user what a PDB ID is and the correct type of a PDB ID 
        print("Every experimental structure in the PDB is assigned a 4-character alphanumeric identifier called the PDB identifier or PDB ID (e.g.2HBS)")

        #allow the user to exit the program if user enters quit, q or Q
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        #display a message to the user indicating exit of the program
        print("Exiting program...")
        break  # Exit the program completely
        #else statement if the user does not quit, to continue with the program
    else:
        #prompts for a PDB ID 
        #while loop that continously prompts user for a PDB ID input raise error if pdb id is not the correct type
        while True:
        #Initial prompt for a PDB ID
            pdb = input("Enter a PDB ID:")
        #check for a valid PDB id if the pdb id is of the correct type and format 
        #if the pdb ID is not of the correct length, it displays a message to the user and continously asks for the valid PDB ID  
            if len(pdb) != 4:
                print("Invalid PDB ID. Enter a 4-character long string e.g 1HIV")
        #if the pdb ID is not in uppercase, prompts user for a valid PDB ID
            elif not pdb.isupper():
                print("Invalid PDB ID. The characters should be uppercase e.g. 1HIV.")
            #checks for at least one number and one letter in the PDB ID   
            elif not re.match("(?=.*[A-Z])(?=.*[0-9])[A-Z0-9]*$", pdb):
                print("Invalid PDB ID. The characters should be alphanumeric e.g. 1HIV")
            else:
                #if all the above statements are False it breaks the loop and continue
                break 
                    
                        
        #if the pdb file is present locally in the machine 
        # defining a function to check if the PDB file exists locally 
        def pdb_check(pdb):
            ''' this function checks is the pdb file is already found locally in the machine or not using os module''' 
            #the filename is given_project to check if the functions correctly downloads the PDB file and not to overwrite any existing pdbfiles 
            filename = f"{pdb.upper()}_project.pdb"
        #return the file path if it exists
            return os.path.exists(filename)
        
        #if the PDB file exists print a message to the user 
        if pdb_check(pdb):
            print("The PDB file is present locally.")

        #if the pdb is not found locally, call the function that downloads the PDB file from the module
        #call the function get_pdb 
        else:
            try:
                #call the function get_pdb with the module pdblib and takes the PDB file as argument 
                get_file = pdblib.get_pdb(pdb)
                #get_pdb uses requests module and URL to download the PDB from RSCB
                #displays a message to the user about the status of the PDB file 
                print("PDB file is not present locally. Downloading the pdb file.....")
                print("PDB file downloaded successfully and saved to local disk")
           
        #if PDB ID does not exists on RCSB, use exception handling to avoid URL HTTPError      
            
            except requests.exceptions.HTTPError as er:
                if er.response.status_code == 404:
                    #if the PDB file not exist, it displays a message to document the user about the PDB ID 
                        print("No such PDB ID exists in the RCSB database\nEvery experimental structure in the PDB is assigned a 4-character alphanumeric identifier called the PDB identifier or PDB ID (e.g.2HBS).\nCheck for a valid PDB ID on the website")
                continue  
        
        #while loop that continously prompts for user input based on a selection of functionalities          
        while True:
            #prompts for a selection based on the menu 
            usr_num = input("Enter a number to select the details or the task you want to perform on the PDB file:")
            
            #if user enter number 1, it displays the header of the PDB file 
            if usr_num == '1':
            #call the read_pdb function that reads and parse the PDB ID as user input 
                details = pdblib.read_pdb(pdb)
            #call the function get_header from the module that reads the file and get the HEADER value 
                header = pdblib.get_header(details)
            #displays the header with the details 
                print("Header:", header + '\n')
            
            #else, if the user enters number 2, it displays the title 
            elif usr_num == '2':
                details = pdblib.read_pdb(pdb)
                title = pdblib.get_title(details)
                #checks for the length of the title, if it is greater than 80 characters, it prints the rest of the line on a newline 
                if len(title) > 80:
                    #creates an empty string new_tlt to store each character of the while title 
                    new_tlt = ''
                    #using a list comprehension to iterate through each character and slicing at 80th character 
                    new_tlt += '\n'.join([title[i:i+80] for i in range (0, len(title), 80)])
                    print("Title:",new_tlt + '\n')
                else:
                    #else if not greater than 80 chars, it prints the title 
                    print("Title:", title + '\n')
            
            elif usr_num == '3':
                details = pdblib.read_pdb(pdb)
                source = pdblib.get_source(details)
                if len(source) > 80:
                    new_source = ''
                    new_source += '\n'.join([source[i:i+80] for i in range(0, len(source), 80)])
                    print("Source:", new_source + '\n')
                else:
                    print("Source:", source + '\n') 
                    
            elif usr_num == '4':
                details = pdblib.read_pdb(pdb)
                keyword = pdblib.get_keyword(details)
                if len(keyword) > 80:
                    new_keyw = ''
                    new_keyw += '\n'.join([keyword[i:i+80] for i in range(0, len(keyword), 80)])
                    print("Keyword:", new_keyw + '\n')
                #else if the length of keywords is not greater than 80, it prints the keywords 
                else:
                    print("Keyword:", keyword + '\n')
            
            elif usr_num == '5':
                details = pdblib.read_pdb(pdb)
                author = pdblib.get_author(details)
                print("Author:",author + '\n')
            
            elif usr_num == '6':
                details = pdblib.read_pdb(pdb)
                res = pdblib.get_resolution(details)
                print("Resolution:",res + '\n')
            
            elif usr_num == '7':
                details = pdblib.read_pdb(pdb)
                journal = pdblib.get_journal(details)
                if len(journal) > 80:
                    new_journal = ''
                    new_journal += '\n'.join([journal[i:i+80] for i in range(0, len(journal), 80)])
                    print("Journal title:", new_journal + '\n')
                else:
                    print("Journal title:",journal + '\n')        
        
            elif usr_num == '8':
                #while loop continously ask for a valid and existing chain ID
                while True:
                    #prompt user for a chain ID
                    chain = input("Enter a chain ID:")
                #statement to check the correct type of chain ID e.g should be a letter and uppercase
                    if chain.isalpha() and chain.isupper():
                #break out of the loop for correct chain ID
                        break
                #if incorrest chain ID is given, it continues the loop and prompts user for a new chain ID 
                    else:
                #if the chain ID is not the correct type it prints message and prompts the user for chain ID again
                        print("Chain ID should be a letter and uppercase e.g A, B, C...")
                        continue
                #display a message to user that the sequence is being retrieved 
                print("Retrieving single letter protein sequence...")
                #calling the function to get the single letter protein residues from the module pdblib 
                protein_seq = pdblib.protein_residue(pdb,chain)
                print("\n")
             
            elif usr_num == '9':
                #while loop continously ask for a valid and existing chain ID
                while True:
                    #prompt user for a chain ID
                    print("If you don't know the chain ID, Press Enter. The chain IDs for the file will be displayed")
                    chain = input("Enter a chain ID:")
                #statement to check the correct type of chain ID e.g should be a letter and uppercase
                    if chain.isalpha() and chain.isupper():
                #break out of the loop for correct chain ID
                        break
                #if no user input,e.g no chain ID is given it breaks the loop and procees to next statement 
                    elif chain == "":
                        break
                #if incorrect chain ID is given, it continues the loop and prompts user for a new chain ID
                    else:
                #if the chain ID is not the correct type it prints message and prompts the user for chain ID again
                        print("Chain ID should be a letter and uppercase e.g A, B, C...")
                        continue
                #calling the function to write the fasta file 
                fasta_file = pdblib.write_fasta(pdb, chain)
                print("\nWriting the FASTA file.....")
                print('\n') 

            elif usr_num == '10':
                #while loop continously ask for a valid and existing chain ID
                while True:
                    #prompt user for a chain ID
                    chain = input("Enter a chain ID:")
                #statement to check the correct type of chain ID e.g should be a letter and uppercase
                    if chain.isalpha() and chain.isupper():
                        break
                    else:
                        print("Chain ID should be a letter and uppercase e.g A, B, C...")
                        continue
                lines_atm_htm = pdblib.extract_lines(pdb,chain)
                print("Writing lines to a file....")

            elif usr_num == '11':
                while True:
                    chain = input("Enter a chain ID:")
                    if chain.isalpha() and chain.isupper():
                        break
                    else:
                        print("Chain ID should be a letter and uppercase e.g A, B, C...")
                        continue

                change_chainID = pdblib.alter_chainID(pdb,chain)

            elif usr_num == '12':
                print("Retrieving any non standard protein residue names...")
                non_standard_residues = pdblib.non_residues(pdb)
                
        
            elif usr_num == '13':
                while True:
                    chain = input("Enter a chain ID:")
                    while True:
                        #prompt user for a plot dimension, use exception handling to check Error 
                        try:
                            #set the input to tuple 
                            plt_dim = tuple(map(int, input("Enter a plot dimension e.g (10,4):").split(",")))
                            if len(plt_dim) != 2:
                                raise ValueError("Plot dimension must be a tuple of length 2")
                            break
                        except ValueError as e:
                            print("Input must be a tuple e.g (10,4) and not a float, integer or string")
                    if chain.isalpha() and chain.isupper():
                        break
                    else:
                        print("Chain ID should be a letter and uppercase e.g A, B, C...")
                        continue
        
                print("Plotting the temperature factor....")
                plotting_temperature = pdblib.plot_temperature(pdb,chain,plt_dim)
                print("use command xdg-open <filename> e.g 2B3P_temp_factor_plot.png to view the plot in the terminal")

            #if the user enters number greater than 13, display a message for option limit 
            elif usr_num > '13':
                print("Number given is beyond the options limit, enter a numerical value between 1-13")
                
    
            #Exiting the selection only if the user inputs the word "quit", the letter "q" or the letter "Q"
            if usr_num.lower() == 'quit' or usr_num.lower() == 'q':
                print("Exiting program.....")
                break  #Exit the loop user enters quit, q, or Q



