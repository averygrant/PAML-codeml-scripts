#PAML-codeml-scripts

This repository contains two scripts to run the codeml program from PAML 4.8 in multiple directories containing a sequence file and control file. Within the bash script, the directory names need to be changed. Currently, the script will loop through all directories ending with a 0. The sequence file name within the bash script also needs to be changed to match the names of the files within all of the directories.

The python script will extract the dN and dS values from the output from codeml and calculate the ratio. Currently the output will be printed to screen but can be changed to save the output to a new file.
