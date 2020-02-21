#! /usr/bin/env python

#Usage: extract dN and dS values from PAML4.8:codeml output file and calculate dN/dS ratios

import re 

InFileName = "alldat.txt" 
InFile = open(InFileName, 'r')

SearchTerm1 = '(\w+\s\w+\s\w+:\s)(PHUM\d+)(\.fasta)'
SearchTerm2 = '(^\s+)(dN\*\=\s+\d\.\d+\s\w+\*\=\s\d+.\d+)' 
SearchTerm3 = '(\s+dN\*\=\s+)(\d+\.\d+)(\s+dS\*\=\s+)(\d+\.\d+)' 

AlldNdS = []  
for Line in InFile:
	print(Line)
	if re.match(SearchTerm1, Line):              
		Name = re.search(SearchTerm1, Line)
	if re.match(SearchTerm2, Line):
		FullLine = re.search(SearchTerm2, Line)               
		Result = re.search(SearchTerm3, Line) 
		dN = (float(Result.group(2)))         
		dS = (float(Result.group(4)))         
		print("Gene Name:", Name.group(2), "dN/dS:", dN/dS)          
		AlldNdS.append(Name.group(2))
		AlldNdS.append(FullLine.group(2))         
print("Raw dN and dS values for each gene:",'\n', AlldNdS)

LineNum = 0
for Item in AlldNdS:
	if not LineNum % 2:
		print(Item, ":", sep=' ', end=' ')
	else:
		print(Item)
	LineNum += 1












     
