#!/usr/bin/python

def binSearch(flist, item):
	if len(flist) == 0:
		return False
	else:
		midpoint = len(flist)//2
		if flist[midpoint] == item:
			return True
		else:
			if item < flist[midpoint]:
				return binSearch(flist[:midpoint], item)
			else:
				return binSearch(flist[midpoint+1:], item)

inlist = [23,445,33,221,211,78,44,22]
inlist.sort()
inp = int(raw_input("Binary Search (Enter): "))
print (binSearch(inlist,inp)) 
