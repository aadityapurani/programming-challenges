from fractions import *

# Euler Phi is like phi(n) where you input n and it displays all integer < n which are relatively prime to n
# generally it gives the total number of integers < n which are relatively prime

n = int(raw_input("n: "))
list_num = []

for x in xrange(1, n):
	val = gcd(x, n)
	if val == 1:
		list_num.append(x)

print list_num
print "Total : "+str(len(list_num))
