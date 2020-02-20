#! /usr/bin/env python

#Usage= In a directory of files, save each file to a new directory with the same name as the file (excluding the file type)

import sys
import re
import os
import shutil

SearchTerm = '(^\w+)(\.\w+\.[a-zA-Z]+(\_)\w+)(\.\w+)'

FileList = sys.argv[1:]
for File in FileList:
	if re.match(SearchTerm, File):
		FullName = re.search(SearchTerm, File)
		os.mkdir(FullName.group(1))
		os.rename(File, FullName.group(1)+FullName.group(4))
	dirnames = next(os.walk('.'))[1]
	filenames = next(os.walk('.'))[2]
	#print(filenames)
	for Dir in dirnames:
		for NewFileName in filenames:
			if NewFileName.startswith(Dir):
				shutil.move(NewFileName, Dir)

SearchTerm3 = '(\[\')(\w+\.\w+)(\'])'


mainwd = os.getcwd() #naming working directory that holds all of the gene files that were just made
#source = os.getcwd()+'/codeml.ctl'  #naming the path to the codeml file
lines = open('codeml.ctl').read().splitlines() #resets for each loop
for Direct in dirnames:                    #for each of the directories in this directory
	LineNumber = 0   #added this line here so it will reset for each file
	os.chdir(Direct) #move into each directory
	Dest = os.getcwd() #set Dest as the path of the current directory
	MessyFileName = next(os.walk('.'))[2] #selects the name of the files in the current directory, there should be only 1 file.
	MessyFileName = str(MessyFileName) #saves variable as string; this is needed so it can be selected by the search term below.
	#print(MessyFileName)
	if re.match(SearchTerm3, MessyFileName):         #SearchTerm3 selects the entire file name
		CleanFileName = re.search(SearchTerm3, MessyFileName)  #save as new variable
		UseThisFileName = (CleanFileName.group(2))    #selecting only part of name (removing square brackets)
	lines[0] = 'seqfile = ' + UseThisFileName
	open('codeml.ctl', 'w').write('\n'.join(lines))
	os.chdir(mainwd)
