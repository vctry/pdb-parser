### Scripts for work with PDB files

###### utils.py 
Main library.
Functions:

- **read_pdb()**: function that takes the name of a .pdb file, 
extracts the coordinates of all the atoms of the protein in a pandas data frame and return it.
- **write_pdb()**: function which takes the name of a .pdb file and a pandas data frame in same format as defined previously and saves it in pdb format.
- **select_atoms()**: function that takes as input a pandas data frame and a selector.
- **get_aa_seq()**: take as argument a pandas data frame and return as a list of string of one letter amino acid sequence.
- **compute_distance()**: function that takes two data frame rows as arguments.


###### contact_map.py
Python script that read a pdb file and split it in multiple files for each of its chains.

Usage example:

    split_chains.py -h 

    split_chains.py -f 3EAM.pdb

###### find_salt_bridges.py

Find all salt bridges in a pandas data frame and return them as a list of residue pairs

Usage example:

    find_salt_bidges.py -h

    find_salt_bidges.py -f ../my_pdb.pdb -o my_pdb_bridges.txt

###### split_chains.py
Plot the contact map a pandas data frame and save it in a file defined by the user

    contact_map.py -h
    
    contact_map.py -f ../my_pdb.pdb -o contact_map.png
    
    contact_map.py -f ../my_pdb.pdb -o contact_map.png -bw #Use bw option for black and white representation


