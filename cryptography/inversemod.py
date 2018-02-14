#!/usr/bin/python
from fractions import *

# Inputs are in form of A^-1 mod N
# Same implementation can be used in Sage as A.inverse_mod(N)
# This is just to know the calculations of satisfying congruence theorem to find the same.
# Test cases: http://www.math.cornell.edu/~mec/Summer2008/lundell/lecture3.html

A = int(raw_input("A: "))
N = int(raw_input("N: "))
iteration = int(raw_input("Iterations: "))
for x in xrange(1, iteration):
    a = x*A
    n = (a-1)%N
    if n==0:
        print "[+] Found "+str(x)
        print str(x)+" X "+str(A)+" congurent 1 (mod "+str(N)+" )"
