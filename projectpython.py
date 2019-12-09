#! /usr/bin/env python

#Usage: extract dN and dS calculations from PAML4.8:codeml output file and calculate dN/dS ratios


import re    #for use of regular expressions

InFileName = "alldat.txt"    #file with codeml output
InFile = open(InFileName, 'r') 

SearchTerm1 = '(\w+\s\w+\s\w+:\s)(PHUM\d+)(\.txt)' #Searches for gene name
SearchTerm2 = '(^\s+dN\*\=\s+\d\.\d+\s\w+\*\=\s\d+.\d+)'  #Searches for line with dN, dS, S, and N calculations 
SearchTerm3 = '(\s+dN\*\=\s+)(\d+\.\d+)(\s+dS\*\=\s+)(\d+\.\d+)' #Seaches and selects for the numbers associated with dN and dS so the ratio can be calculated

AlldNdS = []        #Dictionary to save lines from SearchTerm2
for Line in InFile:
	if re.match(SearchTerm1, Line):                #if searchterm1 matches a line
		Name = re.search(SearchTerm1, Line)    #save search results as 'Name'
	if re.match(SearchTerm2, Line):                #if searchterm2 matches a line
		Result = re.search(SearchTerm3, Line)  #save search results as 'Result'
		dN = (float(Result.group(2)))          #save group 2 from 'Result' as dN
		dS = (float(Result.group(4)))          #save group 4 from 'Result' as dS
		print("Gene Name:", Name.group(2), "dN/dS:", dN/dS)            #print group 2 from 'Name' and dN divided by dS to get the name of the gene, followed by the dN/dS ratio
		AlldNdS.append(Line)                   #append all lines from searchterm2 to AlldNdS dictionary to have record of raw numbers from codeml output
print(AlldNdS)
