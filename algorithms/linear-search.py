#!/usr/bin/python
'''
Linear Search is Simple, you go through every element and compare and see whether we found match or not
Use Better Searching Algorithm lol
'''
flag=0
arr = [12,39,99,92,29,11,44,31]
inp = int(raw_input("Linear Search Algorithm (Enter Number): "))
for x in xrange(0, len(arr)):
	if inp == arr[x]:
		print "[+] Number "+str(inp)+" found at Index "+str(x)+" th Index"
		flag = 1

if flag==0:
	print "[-] Not found"
