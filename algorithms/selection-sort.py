#!/usr/bin/python
'''
Selection Sort
'''

flist = [32, 85, 99, 49, 74, 22]

for x in xrange(1,len(flist)):
	lowest_index = flist.index(min(flist[x:]))
	flist[x-1], flist[lowest_index] = flist[lowest_index], flist[x-1]
	print flist
