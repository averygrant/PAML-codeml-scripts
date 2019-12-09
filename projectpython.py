#! /usr/bin/env python

#Usage: extract dN and dS calculations from PAML4.8:codeml output file and calculate dN/dS ratios


import re    #for use of regular expressions

InFileName = "alldat.txt"    #file with codeml output
InFile = open(InFileName, 'r') 

SearchTerm1 = '(\w+\s\w+\s\w+:\s)(PHUM\d+)(\.txt)' #Searches for gene name
SearchTerm2 = '(^\s+)(dN\*\=\s+\d\.\d+\s\w+\*\=\s\d+.\d+)'  #Searches for line with dN, dS, S, and N calculations 
SearchTerm3 = '(\s+dN\*\=\s+)(\d+\.\d+)(\s+dS\*\=\s+)(\d+\.\d+)' #Seaches and selects for the numbers associated with dN and dS so the ratio can be calculated

AlldNdS = []        #List to save lines from SearchTerm2
for Line in InFile:
	if re.match(SearchTerm1, Line):                #if searchterm1 matches a line
		Name = re.search(SearchTerm1, Line)    #save search results as 'Name'
	if re.match(SearchTerm2, Line):                #if searchterm2 matches a line
		FullLine = re.search(SearchTerm2, Line)
		Result = re.search(SearchTerm3, Line)  #save search results as 'Result'
		dN = (float(Result.group(2)))          #save group 2 from 'Result' as dN
		dS = (float(Result.group(4)))          #save group 4 from 'Result' as dS
		print("Gene Name:", Name.group(2), "dN/dS:", dN/dS)            #print group 2 from 'Name' and dN divided by dS to get the name of the gene, followed by the dN/dS ratio
		AlldNdS.append(Name.group(2))         #append name of file (gene name) to each line in list
		AlldNdS.append(FullLine.group(2))                   #append all lines from searchterm2 to AlldNdS list to have record of raw numbers from codeml output
print("Raw dN and dS values for each gene:",'\n', AlldNdS)   #prints list with all lines containing dN and dS values

LineNum = 0      #setting variable to 0
for Item in AlldNdS:                         #for each line within the AlldNdS list
	if not LineNum % 2:                  #if the linenumber is not divisible by 2 (aka if it is an odd number)
		print(Item, ":", sep=' ', end=' ')     #print that item in the list, add a colon, and separate and end the line with a space so the next line will be printed out on the same line 
	else:
		print(Item)     #if the line is divisible by 2, print line
	LineNum += 1            #add 1 to LineNum for each line








