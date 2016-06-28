#!/bin/python
#Day 5 Loops
#Coded by Aaditya Purani
import sys

x = int(raw_input().strip())
for N in range(1,11):
    print str(x)+" x "+str(N)+" = "+str(x*N)
