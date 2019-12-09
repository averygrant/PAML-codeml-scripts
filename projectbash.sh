#!/bin/bash

#Usage: This script runs the program 'codeml' from PAML4.8 on DNA sequence files in separate directories.


for directory in ./*0/          #Directories in which DNA files and control files are in
do
	cd $directory           #Move into each directory
	echo "OUTPUT FOR FILE:" PHUM*.txt $directory >>../alldat.txt  #Save and append the text document name and the directory name to a text file
	codeml >> ../alldat.txt             #Run the codeml program within each directory and append the output onto the same file.
	cd ..            #Return to one directory up (the directory which holds all the directories of interest)
done
