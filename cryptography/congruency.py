from fractions import *

print "Your form should be a congurent  b (mod n)"
a = int(raw_input("a: "))
b = int(raw_input("b: "))
n = int(raw_input("n: "))

f = (a-b)%n
if f==0:
	print "Congruence relation holds"
else:
	print "Nope"
