#!/bin/python
# Day 3 
#Coded by Aaditya Purani
import sys
N = int(raw_input().strip())
if N%2 != 0:
    print "Weird"
elif (N%2 == 0) & (2<= N <=5):
    print "Not Weird"
elif (N%2 == 0) & (6<= N <=20):
    print "Weird"
elif (N%2 == 0) & (N>=20):
    print "Not Weird"
