#!/bin/python
#Day 11 2D Arrays HackerRank
#Coded by Aaditya Purani

import sys
arr = []
for arr_i in xrange(6):
    ar= map(int,raw_input().strip().split(' '))
    arr.append(ar)
sum=-64
s=0
for i in range(4):
    for j in range(4):
        s=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if(s>sum):
            sum=s
print sum
