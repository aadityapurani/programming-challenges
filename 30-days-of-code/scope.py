#Coded by Aaditya Purani
#HackerRank Scopes
class Difference:
    def __init__(self, a):
        self.__elements = a
              
        self.maximumDifference = 0        
    def computeDifference(self):
        self.maximumDifference = (max(a)-min(a))
        
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference        
