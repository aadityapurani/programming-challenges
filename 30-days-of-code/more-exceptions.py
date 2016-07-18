#Programmed by Aaditya Purani
#Day 17 HackerRank

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
            
        return n ** p
