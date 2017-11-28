#!/usr/bin/python
'''
Ignore the Complexity but wait it's the Bubble Sort
'''

flist= [32, 87, 99, 72, 64]

for x in xrange(0,len(flist)):
	for y in xrange(0, len(flist)):
		if flist[x] < flist[y]:
			flist[x], flist[y] = flist[y], flist[x]

print flist
